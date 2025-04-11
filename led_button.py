#This code was written to control an LED using a pull down resistor
#Written by: Rhea Raoul Date: 10/04/25

#Import necessary libraries
import RPi.GPIO as GPIO
from time import sleep

#Set warnings equal to false
GPIO.setwarnings(False)

#Declare variables
in_pin = 40
out_pin = 38
delay = 0.1

#Set board mode and pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in_pin, GPIO.IN)
GPIO.setup(out_pin, GPIO.OUT)

#Code for turning on and off LCD
try:
    while True:
        read_value = GPIO.input(in_pin)
        sleep(delay)
        #GPIO.output(out_pin, read_value)
        if read_value == 1:
            GPIO.output(out_pin, GPIO.LOW)#can set this to the read_value variable since the return value is techincally a boolean value, high or low, true or false, 1 or 0
        elif read_value == 0:
            GPIO.output(out_pin, GPIO.HIGH)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO pins ready to go!")