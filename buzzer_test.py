#This code was was writen to control simple active buzzer
#Written by: Rhea Raoul Date: 25/03/25

import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
buzzer = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT)
stop = 2

try:
    while True:
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(buzzer,GPIO.LOW)
        sleep(0.1)
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(buzzer, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO good to go!")