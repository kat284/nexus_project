#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                               Information                               %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
#File type:                Nexus Project Python Function File
#File name:                robotCommunication (robotCommunication_BBB.py)
#Description:              Robot communication file for the Pi. Talks to the BBB connected to the Khan chassis and BBB Khan cape.
#Inputs/Resources:         serial
#Output/Created files:     N/A
#Written by:               Keith Tiemann
#Created:                  1/3/2015
#Last modified:            1/3/2016
#Version:                  1.0.0
#Example usage:            N/A
#Notes:  						N/A
#=========================================================================%
#                                 Imports                                 %
#=========================================================================% 
import serial
import time
#=========================================================================%
#                                Functions                                %
#=========================================================================% 
def setupPins():
	port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=None)
	port.close()
	port.open()
def cleanupPins():
	port.close()
def receiveCode():
	 	string = port.read()         
    	time.sleep(0.1)         
    	remaining_bytes = port.inWaiting() 
    	string += port.read(remaining_bytes)
    	return string
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
