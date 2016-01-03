#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                               Information                               %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
#File type:                Nexus Project Python Function File
#File name:                robotMain (robotMain_BBB.py)
#Description:              The main file for the Pi/BBB Khan Chassis. Uses the Khan chassis and BBB Khan cape. The Pi is conntrolled by user input and then controls the BBB.
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
import robotControl_BBB as rC
import time
#=========================================================================%
#                                  Script                                 %
#=========================================================================% 
status = 0
rC.setupPins()
while(status != -1)
	status = talk()
	print status
	
#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                                   End                                   %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
