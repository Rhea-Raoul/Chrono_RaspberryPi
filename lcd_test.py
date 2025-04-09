#importing necessary libraries
import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD

#Set warning modes to false
GPIO.setwarnings(False)

#Set board mode and pins
lcd = CharLCD(cols = 16, rows = 2, pin_rs = 18, pin_e = 23, pins_data = [4, 17, 27, 22], numbering_mode = GPIO.BCM)

#Write to the LCD
#Line 24 to 28 code replacement
lcd.cursor_pos = (0, 1)
lcd.write_string("System loading")
time.sleep(0.5)
for a in range (0, 15):
    lcd.cursor_pos = (0, a)
    lcd.write_string(".")
    time.sleep(0.1)
lcd.clear()

#Line 77 to 80 code replacement
print("Input reset!");
lcd.clear()
lcd.cursor_pos = (0, 5)
lcd.write_string("Clear")
time.sleep(1)

#Line 87 and 88 code replacement
lcd.clear()
lcd.cursor_pos = (0, 3)
lcd.write_string("Successful")

#Line 109 and 110 code replacement
lcd.clear()
lcd.cursor_pos = (0, 3)
lcd.write_string("Wrong PIN!")
time.sleep(0.5)

#Line 151 code replacement
lcd.cursor_pos = (0, 0)
lcd.write_string("Enter your PIN: ")