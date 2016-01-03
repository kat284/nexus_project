#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                               Information                               %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
#File type:                Nexus Project Python Function File
#File name:                robotControl (robotControl_BBB.py)
#Description:              Robot control file for the BBB. Uses the Khan chassis and BBB Khan cape. Does actions based on UART feedback.
#Inputs/Resources:         N/A
#Output/Created files:     N/A
#Written by:               Keith Tiemann
#Created:                  1/3/2016
#Last modified:            1/3/2016
#Version:                  1.0.0
#Example usage:            N/A
#Notes:  
#	Code Abbreviations                  
#		cleanupPins()			=	["cP","1"]
#		rM.leftTrack(speed)	=	["lT"," "]
#		rM.rightTrack(speed)	=	["rT"," "]
#		rM.move(speed)			=	["m" ," "]
#		rM.pointTurn(speed)	=	["pT"," "]
#=========================================================================%
#                                 Imports                                 %
#=========================================================================% 
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.UART as UART
import robotMovement_BBB as rM
import robotCommunication_BBB as rC
import time
#=========================================================================%
#                                Functions                                %
#=========================================================================% 
def setupPins():
	rC.setupPins()
	rM.setupPins()

def cleanupPins():
	rC.cleanupPins()
	rM.cleanupPins()

def runCode(list):
	if ((list(0) == "cP") && (list(1) == "1")):
		cleanupPins():
		return -1
	elif list(0) == "lT":
		rM.leftTrack(speed)
		return 1
	elif list(0) == "rT":
		rM.leftTrack(speed)
		return 1
	elif list(0) == "m":
		rM.move(speed)
		return 1
	elif list(0) == "pT":
		rM.pointTurn(speed)
		return 1
	else:
		return 0

def listen():
	code = [ "00" , '0']
	while code == ['NA', '0']
		code = rC.receiveCode()
	status = runCode(code)
	if status == -1:
		rC.sendCode("-1")
		return -1
	if status == 1:
		rC.sendCode("1")
		return 1
	else:
		rC.sendCode("0")
		return 0

#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                                   End                                   %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
