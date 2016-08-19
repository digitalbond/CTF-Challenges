#!/usr/bin/python
import sys
import getch
import getpass
import os
from cmd2 import Cmd
import time
import serial



def cli_getch():
  pswd = ""
  gc = ""
  while 1:
    gc = getch.getch()
    if gc == "\n":
      break
    pswd += gc
    sys.stdout.write("*")
  return pswd

class Sel(Cmd):
  prompt = '='
  auth_level = 0
  def do_acc(self, arg):
    trynumber = 0
    mytime = time.time()
    myfile = open("Logs/" + mytime.__str__() + ".txt", 'w')
    myfile.write(mytime.__str__() + " : ACC detected\n")
    while (trynumber < 4):
      sys.stdout.write("Password?")
      tpass = cli_getch() #raw_input()
      myfile.write("User enter password: " + tpass)
      myfile.close()
      if tpass == 'OTTER':
        print """

KILLER ROBOTS INC              Date: 01/01/1970        Time: 00:00:00.000
ROBOT PLANT 1                  Time Source: Unknown

Level 1

"""
        acc = Acc()
        acc.echo = True
        acc.cmdloop()
        return
      else:
        trynumber += 1
        print("\nInvalid Password")
        if trynumber > 3:
          print("Alerting the goons!\n\n")
  def default(self, arg):
    print('Invalid Access Level\n')
  def do_help(self, arg):
    print('Invalid Access Level\n')
  def do_set(self, arg):
    self.do_help(arg)
  def do_show(self, arg):
    self.do_help(arg)
  def do_shell(self, arg):
    print('I\'m a-gonna keep my eye on you\n')
class Acc(Sel):
  prompt = '=>'
  auth_level = 1
  def do_EOF(self, args):
    # nope
    # print("caught eof\n")
    return
  def do_help(self, arg):
    print """
ANALOG           - Test an analog output channel. 
BREAKER          - Display breaker monitor data. 
CLOSE            - Close Breaker. 
COMMUNICATIONS   - Display or clear communications channel data. 
CONTROL          - Control Remote Bits and digital outputs. 
COPY             - Copy a settings group into another settings group. 
COUNTERS         - Show current state of device counters.  
ETH              - Display Ethernet Status Report.  
EVENT            - Display an event report. 
EXIT             - Exit to Access Level 0 and terminate the session. 
FILE             - Work with relay files. 
GOOSE            - Display GOOSE Communication Information.
GROUP            - Change a settings Group. 
HISTORY          - Display an event history or clear event data. 
IRIG             - Synchronize the device date and time with the IRIG source. 
LDP              - Display or clear load profile data. 
LOOPBACK         - Test a communications channel. 
MAC              - Display MAC Addresses. 
MAP              - View DNP or Modbus Map 
METER            - Display metering data. 
OPEN             - Open Breaker. 
PING             - Send Ping messages to a network device. 
PULSE            - Pulse a digital output. 
QUIT             - Exit to Access Level 0 
RESTORE_RELAY    - Restore settings to manufacturing default configuration. 
SER              - Display Sequential Events Recorder records. 
SET/SHOW         - Modify or display device settings. 
STATUS           - Display or clear relay status. 
SUMMARY          - Display an event summary. 
TARGETS          - Display internal binary variable values. 
TRIGGER          - Trigger collection of event data.\n\n

CAUTION: For security purposes, some commands are not provided in this HELP
         response.  Elevated privilege, identification, configuration,
         etcetera commands are described in the instruction manual.\n\n"""
  def default(self, arg):
    print('Unknown Command Or Command Not Implemented (Real relays are expensive mkay?)\n\n')
  def do_open(self, arg):
    print('OPEN relay jumper is installed. Destroying the Killer Robots, maybe.\n\n(PS: This is really dangerous, never do this in real life.)\n\n')
  def do_reiddisconnect(self, arg):
    do_exit()
  def do_reidconnect(self, arg):
    do_exit()
  def do_2ac(self, arg):
    print('\n\nPassword? '),
    tpass = cli_getch()
    print('\nINVALID PASSWORD, FLY YOU FOOL\n\n')
  def do_set(self, arg):
    print('Unknown Command\n\n')
  def do_show(self, arg):
    print """

Group 1
Relay Settings

ID Settings
RID      := SET
TID      := LAB PROTECCIONES

Config Settings
CTR      := 10            CTRN     := 10            PTR      := 1.00
DELTA_Y  := WYE           VNOM     := 380.00        SINGLEV  := N

Max Ph Overcurr
50P1P    := 5.00          50P1D    := 0.50
50P1TC   := 1
50P2P    := OFF           50P3P    := 10.00         50P3D    := 0.00
50P3TC   := 1
50P4P    := OFF

Neutral Overcurr
50N1P    := 0.50          50N1D    := 1.00
50N1TC   := 1
50N2P    := OFF           50N3P    := OFF           50N4P    := OFF

Residual Overcurr
50G1P    := 1.50          50G1D    := 1.00
50G1TC   := 1
50G2P    := OFF           50G3P    := OFF           50G4P    := OFF

Neg Seq Overcurr
50Q1P    := OFF           50Q2P    := OFF           50Q3P    := OFF
50Q4P    := OFF

Phase TOC
51AP     := OFF           51BP     := OFF           51CP     := OFF

Maximum Ph TOC
51P1P    := 3.00          51P1C    := U3            51P1TD   := 0.50
51P1RS   := Y             51P1CT   := 1.00          51P1MR   := 0.10
51P1TC   := 1
51P2P    := 6.00          51P2C    := U3            51P2TD   := 3.00
51P2RS   := N             51P2CT   := 0.00          51P2MR   := 0.00
51P2TC   := 1

Negative Seq TOC
51QP     := 6.00          51QC     := U3            51QTD    := 3.00
51QRS    := N             51QCT    := 0.00          51QMR    := 0.00
51QTC    := 1

Neutral TOC
51N1P    := OFF           51N2P    := OFF

Residual TOC
51G1P    := 11.00         51G1C    := U3            51G1TD   := 1.50
51G1RS   := N             51G1CT   := 0.00          51G1MR   := 0.00
51G1TC   := 1
51G2P    := 0.50          51G2C    := U3            51G2TD   := 1.80
51G2RS   := N             51G2CT   := 0.00          51G2MR   := 0.00
51G2TC   := 1

Undervoltage Set
27P1P    := OFF           27P2P    := OFF

Overvoltage Set
59P1P    := OFF           59P2P    := OFF           59G1P    := OFF
59G2P    := OFF           59Q1P    := OFF           59Q2P    := OFF

Power Factor Set
55LGTP   := OFF           55LDTP   := OFF           55LGAP   := OFF
55LDAP   := OFF

Frequency Set
81D1TP   := OFF           81D2TP   := OFF           81D3TP   := OFF
81D4TP   := OFF           81D5TP   := OFF           81D6TP   := OFF

Rate of Frequency Set
E81R     := OFF

Fast Rate of Frequency Set
E81RF    := N

Demand Mtr Set
EDEM     := THM           DMTC     := 5             PHDEMP   := 5.00
GNDEMP   := 1.00          3I2DEMP  := 1.00

Power Elements
EPWR     := N

Trip/Close Logic
TDURD    := 0.0           CFD      := 1.0
TR       := ORED50T OR ORED51T OR 81D1T OR 81D2T OR 81D3T OR 81D4T OR 59P1T OR
            59P2T OR 55T OR REMTRIP OR SV01 OR OC OR SV04T OR 50P1P
REMTRIP  := 0
ULTRIP   := NOT ( 51P1P OR 51G1P OR 51N1P OR 52A )
52A      := 0
CL       := SV03T AND LT02 OR CC
ULCL     := 0

Reclosing Control
E79      := OFF

"""
  def do_status(self, arg):
    print """
KILLER ROBOTS INC              Date: 01/01/1970        Time: 00:00:00.000
ROBOT PLANT 1                  Time Source: Unknown

Serial Num = 1380926031     FID = SEL-751A-R419-V0-Z011003-D20131025
CID = 79CC                  PART NUM = 751A61A1A0X74850330

SELF TESTS (W=Warn)
  FPGA  GPSB  HMI   RAM   ROM   CR_RAM  NON_VOL  CLOCK  CID_FILE  +0.9V  +1.2V
  OK    OK    OK    OK    OK    OK      OK       OK     OK        0.91   1.20

  +1.5V  +1.8V  +2.5V  +3.3V  +3.75V  +5.0V  -1.25V  -5.0V   BATT
  1.50   1.81   2.51   3.32   3.77    4.97   -1.25   -4.92   3.03

Option Cards
  CARD_C  CARD_D  CARD_E  CURRENT
  OK      OK      OK      OK

Offsets
   IA    IB    IC    IN    VA    VB    VC
  6     6     5     6     0     0     0

  Relay Enabled

"""

#ser = serial.Serial("/dev/ttyAMA0", baudrate=115200)
#sys.stdout = ser.fileno()
#sys.stdin = ser.fileno()

sel = Sel()
sel.echo = True
sel.cmdloop()
