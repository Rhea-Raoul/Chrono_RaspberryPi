import RPi.GPIO as GPIO
import time


def init_keypad():
    global C1, C2, C3, C4
    global R1, R2, R3, R4

    # Enter column pins
    C1 = 12
    C2 = 16
    C3 = 20
    C4 = 21
    # Enter row pins
    R1 = 6
    R2 = 13
    R3 = 19
    R4 = 26

    # Set column pins as output pins
    GPIO.setup(C1, GPIO.OUT)
    GPIO.setup(C2, GPIO.OUT)
    GPIO.setup(C3, GPIO.OUT)
    GPIO.setup(C4, GPIO.OUT)
    # Set row pins as input pins
    GPIO.setup(R1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(R2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(R3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(R4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Detect the rising edges
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
    elif mode == 2:
        if keypadPressed_code == -1:
            keypadPressed_code = channel


#Sets all rows to a specific state. 
def setAllRows(state):
    GPIO.output(C1, state)
    GPIO.output(C2, state)
    GPIO.output(C3, state)
    GPIO.output(C4, state)

# Check or clear PIN


# reads the columns and appends the value, that corresponds
# to the button, to a variable
def read(column, characters):
    global input, user_id, mode
    GPIO.output(column, GPIO.HIGH)
    if(GPIO.input(R1) == 1):
        if mode == 1:
            user_id = user_id + characters[0]
            print(user_id)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(str(user_id))
        elif mode == 2:
            input = input + characters[0]
            print(input)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(str(input))
    if(GPIO.input(R2) == 1):
        if mode == 1:
            input = user_id + characters[1]
            print(user_id)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(str(user_id))
        elif mode == 2:
            input = input + characters[1]
            print(input)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(str(input))
    if(GPIO.input(R3) == 1):
        if mode == 1:
            input = user_id + characters[2]
            print(user_id)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(str(user_id))
        elif mode == 2:
            input = input + characters[2]
            print(input)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(str(input))
    if(GPIO.input(R4) == 1):
        if mode == 1:
            input = user_id + characters[3]
            print(user_id)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(str(user_id))
        elif mode == 2:
            input = input + characters[2]
            print(input)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(str(input))
    GPIO.output(column, GPIO.LOW)
