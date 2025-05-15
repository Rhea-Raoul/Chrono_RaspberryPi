#Import necessary libraries
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time

#LCD initialization function
def init_lcd():
    global lcd 
    lcd = CharLCD(cols = 16, rows = 2, 
                pin_rs = 18, pin_e = 23, 
                pins_data = [24, 17, 27, 22],
                numbering_mode = GPIO.BCM)
    lcd.clear()
    return lcd

#Function responsible for writing to the LCD
def write_lcd(row, col, msg):
    lcd.cursor_pos = (row, col)
    lcd.write_string(msg)
    time.sleep(0.01)

#Function for clearing the LCD
def clear_lcd():
    lcd.clear()
    time.sleep(0.2)
