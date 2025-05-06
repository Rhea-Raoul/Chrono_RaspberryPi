import RPi.GPIO as GPIO
import time


def init_System(lcd):

    # Setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #Starting text
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



