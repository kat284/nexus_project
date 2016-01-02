#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                               Information                               %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
#File type:                Nexus Project Python Function File
#File name:                robotControl (robotControl_BBB.py)
#Description:              Robot control file for the BBB. Uses the Khan chassis and BBB Khan cape.
#Inputs/Resources:         pyserial
#Output/Created files:     N/A
#Written by:               Keith Tiemann
#Created:                  12/28/2015
#Last modified:            12/31/2015
#Version:                  1.0.0
#Example usage:            N/A
#Notes:                    
# UART	RX	TX	CTS	RTS	Device
# UART1	P9_26	P9_24	P9_20	P9_19	/dev/ttyO1
# UART2	P9_22	P9_21			/dev/ttyO2
# UART3		P9_42	P8_36	P8_34	/dev/ttyO3
# UART4	P9_11	P9_13	P8_35	P8_33	/dev/ttyO4
# UART5	P8_38	P8_37	P8_31	P8_32	/dev/ttyO5
#=========================================================================%
#                                 Imports                                 %
#=========================================================================% 
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.UART as UART
#=========================================================================%
#                                Functions                                %
#=========================================================================% 
def setupPins():
	UART.setup("UART5")
def cleanupPins():
	PWM.cleanup()	
	GPIO.cleanup()

#  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .%
#:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::%
#'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'  %
#                                   End                                   %
#'      .--.      .'-.      .--.      .--.      .--.      .-'.      .--.  %
#:::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::::'/::::::%
#  `--'      `-.'      `--'      `--'      `--'      `--'      `.-'      `%
