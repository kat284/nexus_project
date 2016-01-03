#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                               Information                               %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
#File type:                Nexus Project Python Function File
#File name:                robotCommunication (robotCommunication_BBB.py)
#Description:              Robot communication file for the BBB. Uses the Khan chassis and BBB Khan cape.
#Inputs/Resources:         pyserial
#Output/Created files:     N/A
#Written by:               Keith Tiemann
#Created:                  12/28/2015
#Last modified:            1/3/2016
#Version:                  1.0.0
#Example usage:            N/A
#Notes:  						N/A
#=========================================================================%
#                                 Imports                                 %
#=========================================================================% 
import Adafruit_BBIO.UART as UART
import time
#=========================================================================%
#                                Functions                                %
#=========================================================================% 
def setupPins():
	UART.setup("UART5")
	port = serial.Serial(port = "/dev/ttyO5", baudrate=9600)
	port.close()
	port.open()
def cleanupPins():
	port.close()
	PWM.cleanup()	
	GPIO.cleanup()
def receiveCode():
	try:
		string = port.read()         
	   time.sleep(0.1)         
	   remaining_bytes = port.inWaiting() 
	   string += port.read(remaining_bytes)
		list = string.split('._.')
	   return list
	except:
	   return ['NA', '0']
def sendCode(string):
	if port.isOpen():
    	 port.write(string)
	    time.sleep(0.1)	

#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                                   End                                   %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
