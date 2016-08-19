package main

import (
	"fmt"
	"io"
	"os/exec"
	"log"
	"github.com/tarm/serial"
	"github.com/traetox/goGPIO"
	"time"
)

const (
	unbuffer = "/usr/bin/unbuffer"
	dashp = "-p"
	selpy = "/home/pi/sel.py"
	bluetoothpin = 26
)

func pinMonitor(pin *goGPIO.GPIO, in io.WriteCloser, term *serial.Port) {
	sleeptimer := 500 * time.Millisecond
	exitcmd := []byte("\n\n\n\nexit\nexit\n")
	modemkill1 := []byte("$$$") // kill the remote connection if he is monopolizing
	modemkill2 := []byte("K,\n")
	warningmsg := []byte("***ONE MINUTE WARNING. SOLVE THE FLAG OR LOG OFF THE BLUETOOTH PLZ.***\r\n\r\n")
	timeoutmsg := []byte("Sorry pal, time's up. If you didn't solve it, think a while and try again.\r\n\r\n")
	starttime := time.Now()
	displayedwarning := false
	for {
		sessiontime := time.Since(starttime)
		if sessiontime > (5 * time.Minute) {
			term.Write(timeoutmsg)
			time.Sleep(1200*time.Millisecond)
			term.Write(modemkill1)
			time.Sleep(1200*time.Millisecond)
			term.Write(modemkill2)
		}
		if (sessiontime > (4 * time.Minute)) && (displayedwarning == false)  {
			term.Write(warningmsg)
			displayedwarning = true
		}

		g, err := goGPIO.New(bluetoothpin)
		if err != nil {
			panic(err)
		}
		g.SetInput()
		pinState := g.State()
		if pinState != true {
			fmt.Println("GPIO pin went low, exiting pinMonitor")
			in.Write(exitcmd)
			break
		}
		time.Sleep(sleeptimer)
	}
}

func main() {
	c := &serial.Config{Name: "/dev/ttyAMA0", Baud: 9600}
		s, err := serial.OpenPort(c)
		if err != nil {
			log.Fatal(err)
	}
	// confusing =). GPIO26 is WiringPi pin 25.
	// GPIO12 is wiringpi 26.  So I just hooked up GPIO26 *and* GPIO12
	// to the GPIO2 on the bluetooth and it should work
	g, err := goGPIO.New(bluetoothpin)
	if err != nil {
		panic(err)
	}
	g.SetInput()
	sleeptimer := 500 * time.Millisecond
	for {
		fmt.Println("Starting up!")
		cmd := exec.Command(unbuffer, dashp, selpy)
		in, err := cmd.StdinPipe()
		if err != nil {
			panic(err)
		}
		//defer in.Close()
		out, err := cmd.StdoutPipe()
		if err != nil {
			panic(err)
		}
		//defer out.Close()
		// start the process
		if err = cmd.Start(); err != nil {
			panic(err)
		}
		// connect the pipes, otherwise the GPIO doesn't report the right state?
		go io.Copy(in, s)
		go io.Copy(s, out)
		// loop until we get a pin high...
		fmt.Println("Waiting for connection")
		for {
		        g, err := goGPIO.New(bluetoothpin)
       			if err != nil {
                		panic(err)
        		}
			g.SetInput()
			pinState := g.State()
			if pinState != false {
				fmt.Println("Got connection!")
				break
			}
			time.Sleep(sleeptimer)
		}
		fmt.Println("Got connection")
		pinMonitor(g, in, s)
		fmt.Println("Closing out!")
		// if we return, close in and out
		in.Close()
		out.Close()
	}
}
