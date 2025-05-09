import RPi.GPIO as GPIO
import time


def init_buzzer():
    # Enter buzzer pin
    global buzzer_pin 
    buzzer_pin = 4
    GPIO.setup(buzzer_pin,GPIO.OUT)


def buzzer_beep(buzzer_time):
    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(buzzer_time)
    GPIO.output(buzzer_pin,GPIO.LOW)
    time.sleep(buzzer_time)
