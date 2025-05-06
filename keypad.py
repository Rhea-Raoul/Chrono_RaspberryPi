#Import the necessary libraries
import RPi.GPIO as GPIO
#Set pins
#Column pins
C1 = 12
C2 = 16
C3 = 20
C4 = 21
#Row pins
R1 = 6
R2 = 13
R3 = 19
R4 = 26

def setAllRows(state):
    GPIO.output(C1, state)
    GPIO.output(C2, state)
    GPIO.output(C3, state)
    GPIO.output(C4, state)

def keypadCallback(channel):
    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel