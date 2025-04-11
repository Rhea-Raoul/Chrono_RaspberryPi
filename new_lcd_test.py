#This code was written to control an lcd with simple commands
#Written by: Rhea Raoul Date: 09/04/25

#Import libraries
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
from time import sleep

#Set GPIO warnings to false
GPIO.setwarnings(False)

#Create lcd object and set pins and board mode
lcd = CharLCD(cols = 16, rows = 2, pin_rs = 18, pin_e = 23, pins_data = [24, 17, 27, 22],numbering_mode = GPIO.BCM)

#Set the cursor position, write the screen "Hello World", then wait two seconds and clear the screen
lcd.clear()
sleep(1)
lcd.write_string("yellow")
sleep(1)
lcd.clear()