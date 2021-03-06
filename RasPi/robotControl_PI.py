#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                               Information                               %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
#File type:                Nexus Project Python Function File
#File name:                robotControl (robotControl_Pi.py)
#Description:              Robot control file for the Pi. Talks to the BBB connected to the Khan chassis and BBB Khan cape.
#Inputs/Resources:         N/A
#Output/Created files:     N/A
#Written by:               Keith Tiemann
#Created:                  1/3/2016
#Last modified:            1/3/2016
#Version:                  1.0.0
#Example usage:            N/A
#Notes:  
#	Code Abbreviations                  
#		BBB did nothing			=	"0"
#		BBB shutting down			=	"-1"
#		BBB did something			=	"1"
#		Pi did nothing				=	"00"
#=========================================================================%
#                                 Imports                                 %
#=========================================================================% 
import robotCommunication_Pi as rC
import time
#=========================================================================%
#                                Functions                                %
#=========================================================================% 
def setupPins():
	rC.setupPins()

def cleanupPins():
	rC.cleanupPins()

def runCode(status):
	if status == "-1":
		cleanupPins()
		return '-1'
	elif status == "1":
		return '1'
	elif status == "0":
		return '0'
	else:
		return '00'

def talk():
	print('shutdown BBB						=	cP._.1')
	print('move left track with speed	=	lT._.x')
	print('move right track with speed	=	rT._.x')
	print('move tracks with speed			=	m._.x')
	print('point turn with speed			=	pT._.x')
	scode = raw_input("What Action should be done? ").strip("\r\n")
	rC.sendCode(scode)
	time.sleep(.2)
	code = rC.receiveCode()
	status = runCode(code)

#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                                   End                                   %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
