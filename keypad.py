#Import the necessary libraries
import RPi.GPIO as GPIO
import time
from lcd import *

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

keypadPressed = -1

#Input, User ID, passcode and string variables are set to empty
#so that they can be used to store the values
input = ""
userId = ""
passCode = ""
str = ""

#Keypad intiliazation function which sets columns and row pins to output and input repesctively
def init_keypad():
    # The GPIO pin of the column of the key that is currently
    # being held down or -1 if no key is pressed
    global C1, C2, C3, C4
    global R1, R2, R3, R4
    
    # Setting column pins as output pins
    GPIO.setup(C1, GPIO.OUT)
    GPIO.setup(C2, GPIO.OUT)
    GPIO.setup(C3, GPIO.OUT)
    GPIO.setup(C4, GPIO.OUT)
    
    # Setting row pins as input pins
    GPIO.setup(R1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(R2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(R3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(R4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


    # Adding event detection so that when a key is pressed the keypadcallback function is able to record it
    GPIO.add_event_detect(R1, GPIO.RISING, callback=keypadCallback)
    GPIO.add_event_detect(R2, GPIO.RISING, callback=keypadCallback)
    GPIO.add_event_detect(R3, GPIO.RISING, callback=keypadCallback)
    GPIO.add_event_detect(R4, GPIO.RISING, callback=keypadCallback)


# This callback registers the key that was pressed
# if no other key is currently pressed
def keypadCallback(channel):

    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel
    

#Sets all rows to a specific state. 
def setAllRows(state):
    GPIO.output(C1, state)
    GPIO.output(C2, state)
    GPIO.output(C3, state)
    GPIO.output(C4, state)
    
#Reads the columns and appends the value, that corresponds
#to the button, to a variable
def read(column, characters):

    res = ""
    GPIO.output(column, GPIO.HIGH)
    if(GPIO.input(R1) == 1):
        res = characters[0]
    elif(GPIO.input(R2) == 1):
        res = characters[1]
    elif (GPIO.input(R3) == 1):
        res = characters[2]
    elif (GPIO.input(R4) == 1):
        res = characters[3]

    GPIO.output(column, GPIO.LOW)
    
    return res

#Function to check if the CLEAR key is pressed 
def is_clear_key_pressed():
    # CLEAR Key
    GPIO.output(C4, GPIO.HIGH)
    if (GPIO.input(R3) == 1):
        GPIO.output(C4, GPIO.LOW)
        return True
    GPIO.output(C4, GPIO.LOW)
    return False

#Function to check if the ENTER key is pressed
def is_enter_key_pressed():
        # Check ENTER Key
    GPIO.output(C4, GPIO.HIGH)
    if (GPIO.input(R4) == 1):
        GPIO.output(C4, GPIO.LOW)
        return True
    GPIO.output(C4, GPIO.LOW)
    return False


#This function determines which key(s) was pressed then executes the corresponding logic, whether it be to clear,
#enter or read the keys being pressed by the user
def read_from_keypad():

    global keypadPressed
    global input 

    if (keypadPressed != -1):
        setAllRows(GPIO.HIGH)

        if not GPIO.input(keypadPressed):
            keypadPressed = -1

    else:
        if is_clear_key_pressed():
            input = ""
            return "clear"
        elif is_enter_key_pressed():
            input = ""
            return "enter"
        else:
            input += read(C1, ["1","4","7","*"])
            input += read(C2, ["2","5","8","0"])
            input += read(C3, ["3","6","9","#"])
            input += read(C4, ["A","B","C","D"])


    time.sleep(0.1)

    return input

