#Import the necessary libraries 
import RPi.GPIO as GPIO
import time

#Function responsible for initializing the buzzer
def init_buzzer():
    # Enter buzzer pin
    global buzzer_pin 
    buzzer_pin = 4
    GPIO.setup(buzzer_pin,GPIO.OUT)
    GPIO.output(buzzer_pin,GPIO.LOW)

#Function responsible for beeping the buzzer
# The buzzer will beep for the time specified in the buzzer_time variable
def buzzer_beep(buzzer_time):
    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(buzzer_time)
    GPIO.output(buzzer_pin,GPIO.LOW)
    time.sleep(buzzer_time)
