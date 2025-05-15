#Import the necessary libraries
import RPi.GPIO as GPIO
import time

#System init function which sets GPIO warnings, pin numbering mode, and also the code responsible for displaying the system
#loading message on the LCD
def init_System(lcd):

    # Setup GPIO warnings and pin numbering mode
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #System loading message
    lcd.clear()
    time.sleep(0.5)
    lcd.cursor_pos = (0, 1)
    lcd.write_string("System loading")
    time.sleep(0.5)
    for a in range (0, 15):
        lcd.cursor_pos = (0, a)
        lcd.write_string(".")
        time.sleep(0.2)
    time.sleep(0.5)
    lcd.clear()



