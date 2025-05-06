import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
relay = 25
relay_state = False
GPIO.setup(relay, GPIO.OUT)

try:
    if relay_state == False:
        GPIO.output(relay, GPIO.HIGH)
        sleep(3)
        GPIO.output(relay, GPIO.LOW)
    relay_state = True
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nWe're Animaniacs")