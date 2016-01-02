#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                               Information                               %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
#File type:                Nexus Project Python Function File
#File name:                robotMovement (robotMovement_BBB.py)
#Description:              Robot control file for the BBB. Uses the Khan chassis and BBB Khan cape.
#Inputs/Resources:         N/A
#Output/Created files:     N/A
#Written by:               Keith Tiemann
#Created:                  12/28/2015
#Last modified:            12/28/2015
#Version:                  1.0.0
#Example usage:            N/A
#Notes:                    There are four basic movement functions, leftTrack, rightTrack, move and pointTurn. For swing turns or wide turns, it's better for them to be in more advanced code as normally those turns aren't needed a lot.
#=========================================================================%
#                                 Imports                                 %
#=========================================================================% 
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
#=========================================================================%
#                                Functions                                %
#=========================================================================% 
def setupPins():
	GPIO.setup("P9_11", GPIO.OUT) # AIN2 Front Left Wheel
	GPIO.setup("P9_12", GPIO.OUT) # AIN1 Front Left Wheel
	GPIO.setup("P9_13", GPIO.OUT) # BIN1 Back Left Wheel
	GPIO.setup("P9_15", GPIO.OUT) # BIN2 Back Left Wheel
	GPIO.setup("P9_17", GPIO.OUT) # LV1
	GPIO.setup("P9_18", GPIO.OUT) # LV2
	GPIO.setup("P9_23", GPIO.OUT) # AIN2 Front Right Wheel
	GPIO.setup("P9_41", GPIO.OUT) # AIN1 Front Right Wheel
	GPIO.setup("P9_24", GPIO.OUT) # BIN1 Back Right Wheel
	GPIO.setup("P9_26", GPIO.OUT) # BIN2 Back Right Wheel
	GPIO.setup("P9_27", GPIO.OUT) # LV3
	GPIO.setup("P9_30", GPIO.OUT) # LV4
	PWM.start("P9_14", 0) # PWMA Left Wheels
	PWM.start("P9_16", 0) # PWMB Left Wheels
	PWM.start("P9_21", 0) # PWMA Right Wheels
	PWM.start("P9_22", 0) # PWMB Right Wheels
def cleanupPins():
	PWM.cleanup()	
	GPIO.cleanup()
def leftTrack(speed): #Speed is from -100.0 to 100.0
	if (speed > 0):
		GPIO.output("P9_11", GPIO.LOW)
		GPIO.output("P9_12", GPIO.HIGH)
		GPIO.output("P9_13", GPIO.LOW)
		GPIO.output("P9_15", GPIO.HIGH)
		PWM.start("P9_14", speed)
		PWM.start("P9_16", speed)
	elif (speed < 0):
		GPIO.output("P9_11", GPIO.HIGH)
		GPIO.output("P9_12", GPIO.LOW)
		GPIO.output("P9_13", GPIO.HIGH)
		GPIO.output("P9_15", GPIO.LOW)
		PWM.start("P9_14", -speed)
		PWM.start("P9_16", -speed)
	else:
		GPIO.output("P9_11", GPIO.LOW)
		GPIO.output("P9_12", GPIO.LOW)
		GPIO.output("P9_13", GPIO.LOW)
		GPIO.output("P9_15", GPIO.LOW)
		PWM.start("P9_14", 0)
		PWM.start("P9_16", 0)
def rightTrack(speed): #Speed is from -100.0 to 100.0
	if (speed > 0):
		GPIO.output("P9_24", GPIO.HIGH)
		GPIO.output("P9_26", GPIO.LOW)
		GPIO.output("P9_23", GPIO.HIGH)
		GPIO.output("P9_41", GPIO.LOW)
		PWM.start("P9_21", speed)
		PWM.start("P9_22", speed)
	elif (speed < 0):
		GPIO.output("P9_24", GPIO.LOW)
		GPIO.output("P9_26", GPIO.HIGH)
		GPIO.output("P9_23", GPIO.LOW)
		GPIO.output("P9_41", GPIO.HIGH)
		PWM.start("P9_21", -speed)
		PWM.start("P9_22", -speed)
	else:
		GPIO.output("P9_24", GPIO.LOW)
		GPIO.output("P9_26", GPIO.LOW)
		GPIO.output("P9_23", GPIO.LOW)
		GPIO.output("P9_41", GPIO.LOW)
		PWM.start("P9_21", 0)
		PWM.start("P9_22", 0)
def move(speed): #Move only fowards and backwards
	leftTrack(speed)
	rightTrack(speed)
def pointTurn(speed): #Only left and right point turns.
	leftTrack(-speed)
	rightTrack(speed)
#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                                   End                                   %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
