import RPi.GPIO as GPIO

Relay = 25
relayState = False

def init_relay():
    global Relay 
    global relayState

    Relay = 25
    relayState = False
    GPIO.setup(Relay,GPIO.OUT)
    GPIO.output(Relay,GPIO.LOW)
