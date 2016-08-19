= DO NOT USE THIS AS A PRODUCTION HONEYPOT
= DO NOT USE THIS AS A PRODUCTION HONEYPOT
= DO NOT USE THIS AS A PRODUCTION HONEYPOT

= SEL Emulator

== About
This is a pretty rudimentary 'SEL Emulator'. It was designed for use in the
S4 (SCADA Security Scientific Symposium) conference in 2016. Players were
tasked with identifying a digital protective relay, left available via a
wireless connection.

This project simulates an SEL-2924 Bluetooth to Serial adapter, as it would
appear if it was accidentally left connected to a SEL-751A Feeder protection
relay. Both the Bluetooth adapter and the SEL relay feature their default
passwords (PIN pairing code 2924 for the Bluetooth, and OTTER/TAIL as the
relay level 1 and level 2 passwords, respectively).

The sel.py Python script acts as the SEL-751A relay emulator. Note that this
uses the Python cmd2 package for building a command line, and that it contains
vulnerabilities. Specifically, an attacker may gain a command line on your
system with the privileges of the Python process. On a Raspberry Pi system with
default configuration, an attacker could easily get root privileges on the Pi.

== Installation

There are two methods of using the honeypot.  The first method is to use the
device as a Bluetooth honeypot.  The second method is to use it as a TCP (TELNET) honeypot.

Again, do not use this in production.  There are security vulnerabilities both known and unknown in the implementation.  The CMD2 library features many backdoor commands, and an attacker can easily root your Raspberry Pi or any *nix system that you run this code on.

=== Install as a Bluetooth device
To install this project you will need a bluetooth adapter on your Raspberry Pi.
This code depends upon features of an external Bluetooth Serial adapter. Specifically, you should use the Roving Networks RN-42.

Connect the RN42 pin PIO2 to GPIO26 *and* GPIO12 on the Raspberry Pi GPIO block.

Connect the RN42 TX and RX pins to the serial GPIO pins on the Raspberry Pi, and connect the RN42 3.3v and GND pins to the 3.3v and GND pins on the Raspberry Pi.

Copy the file 'etc/init/sel-emulator.conf' to your Pi's /etc/init/ directory.

Copy the file 'home/pi/sel.py' to your Pi's /home/pi directory.

Copy the file 'home/pi/serialcode/serialtest.go' to your Pi's /home/pi/serialcode directory (create this directory if it does not exist).

Modify the serialtest.go file so that the line 59 'Name' variable is assigned.
to your Raspberry Pi's bluetooth adapter.  Change the 'Baud' variable to the baud rate of your Bluetooth adapter.  You may wish to verify that you can communicate with your RN42 adapter at this stage, using your favorite terminal software (we use screen).

Modify the PIN and SSID of the RN42. See the RN42 instruction manual for help on the commands to achieve this.

Disable the Serial Console on the Raspberry Pi serial port by modifying the /boot/config.txt.  Ensure that the boot variable 'console' is set to something other than the Bluetooth's serial port.  For example.

On our test Raspberry Pi 2, we leave the serialtest.go file alone (using /dev/ttyAMA0 as the bluetooth port), and set the boot line to be:

dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait

You should now be able to reboot your Pi. You should now see the Bluetooth device as pairable.  Pair with your PIN, and you may open a serial terminal on your laptop.  Press the 'enter' key to see the classic SEL '=' prompt, indicating that you are logged in with no authentication.

=== Installation as a TCP Service

TODO =).  You can just wrap the sel.py script in a netcat server call, if you wish, as 'nc -l -k -p 23 -e python /path/to/sel.py'.  For slightly better security, it may be better to run this as a service with 'nobody/nogroup' privileges. We will post instructions soon.
