import RPi.GPIO as GPIO


def init_relay():

    # Enter RELAY pin
    global Relay 
    global relayState

    Relay = 25
    relayState = False
    GPIO.setup(Relay,GPIO.OUT)
