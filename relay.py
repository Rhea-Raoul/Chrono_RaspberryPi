#Import the necessary libraries
import RPi.GPIO as GPIO

#Set relay pin and relay state
Relay = 25
relayState = False

#Relay initialization function
def init_relay():
    global Relay 
    global relayState

    Relay = 25
    relayState = False
    GPIO.setup(Relay,GPIO.OUT)
    GPIO.output(Relay,GPIO.LOW)
