#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                               Information                               %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
#File type:                Nexus Project Python Function File
#File name:                robotMain (robotMain_BBB.py)
#Description:              The main file for the BBB's Khan Chassis. Uses the Khan chassis and BBB Khan cape.
#Inputs/Resources:         N/A
#Output/Created files:     N/A
#Written by:               Keith Tiemann
#Created:                  1/3/2016
#Last modified:            1/3/2016
#Version:                  1.0.0
#Example usage:            N/A
#Notes:  						N/A
#=========================================================================%
#                                 Imports                                 %
#=========================================================================% 
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import robotControl_BBB as rC
import time
#=========================================================================%
#                                  Script                                 %
#=========================================================================% 
status = 0
rC.setupPins()
while(status != -1)
	status = listen()
	
#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                                   End                                   %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
