# Include the library files
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time
import requests
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
# Enter buzzer pin
buzzer = 4
# Enter LED pin
Relay = 27
relayState = True
# Create a object for the LCD
lcd = CharLCD(cols = 16, rows = 2, pin_rs = 18, pin_e = 23, pins_data = [24, 17, 27, 22],numbering_mode = GPIO.BCM)
#Starting text
lcd.cursor_pos = (0, 1)
lcd.write_string("System loading")
time.sleep(0.5)
for a in range (0, 15):
    lcd.cursor_pos = (0, a)
    lcd.write_string(".")
    time.sleep(0.2)
lcd.clear()
# The GPIO pin of the column of the key that is currently
# being held down or -1 if no key is pressed
keypadPressed = -1
# Enter your PIN
secretCode = "1234"
input = ""
# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(Relay,GPIO.OUT)
GPIO.output(Relay,GPIO.HIGH)
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
# This callback registers the key that was pressed
# if no other key is currently pressed
def keypadCallback(channel):
    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel
# Detect the rising edges
GPIO.add_event_detect(R1, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(R2, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(R3, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(R4, GPIO.RISING, callback=keypadCallback)
# Sets all rows to a specific state. 
def setAllRows(state):
    GPIO.output(C1, state)
    GPIO.output(C2, state)
    GPIO.output(C3, state)
    GPIO.output(C4, state)
# Check or clear PIN
def commands():
    global relayState
    global input
    pressed = False
    GPIO.output(C4, GPIO.HIGH)
    
    # Clear PIN 
    if (GPIO.input(R3) == 1 ):
        print("Input reset!");
        lcd.clear()
        lcd.cursor_pos = (0, 5)
        lcd.write_string("Clear")
        time.sleep(1)
        pressed = True
    GPIO.output(C4, GPIO.HIGH)
    # Check PIN
    if (not pressed and GPIO.input(R4) == 1):
        secretCode = requests.get("http://172.19.16.23:5000/access_request/%s/%s" % ('23', input))
        #print(url) 
        #secretCode = requests.get('http://172.19.16.23:5000/access_request/',params={'id': '23', 'code': input})
        print(secretCode)

        if secretCode == 'True':
            lcd.clear()
            lcd.cursor_pos = (0, 3)
            lcd.write_string("Successful")
            
            if relayState == False:
                GPIO.output(Relay,GPIO.HIGH)
                GPIO.output(buzzer,GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(buzzer,GPIO.LOW)
                time.sleep(0.3)
                relayState = True
                
            elif relayState:
                GPIO.output(Relay,GPIO.LOW)
                GPIO.output(buzzer,GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(buzzer,GPIO.LOW)
                time.sleep(1)
                relayState = False
                  
            
        else:
            print("Incorrect code!")
            lcd.clear()
            lcd.cursor_pos = (0, 3)
            lcd.write_string("Wrong PIN!")
            time.sleep(0.5)
            GPIO.output(buzzer,GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(buzzer,GPIO.LOW)
            time.sleep(0.3)
            GPIO.output(buzzer,GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(buzzer,GPIO.LOW)
            time.sleep(0.3)
            GPIO.output(buzzer,GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(buzzer,GPIO.LOW) 
        pressed = True
    GPIO.output(C1, GPIO.LOW)
    if pressed:
        input = ""
    return pressed
# reads the columns and appends the value, that corresponds
# to the button, to a variable
def read(column, characters):
    global input
    GPIO.output(column, GPIO.HIGH)
    if(GPIO.input(R1) == 1):
        input = input + characters[0]
        print(input)
        lcd.cursor_pos = (1, 0)
        lcd.write_string(str(input))
    if(GPIO.input(R2) == 1):
        input = input + characters[1]
        print(input)
        lcd.cursor_pos = (1, 0)
        lcd.write_string(str(input))
    if(GPIO.input(R3) == 1):
        input = input + characters[2]
        print(input)
        lcd.cursor_pos = (1, 0)
        lcd.write_string(str(input))
    if(GPIO.input(R4) == 1):
        input = input + characters[3]
        print(input)
        lcd.cursor_pos = (1, 0)
        lcd.write_string(str(input))
    GPIO.output(column, GPIO.LOW)
try:
    while True:       
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Enter your PIN: ")
        
        # If a button was previously pressed,
        # check, whether the user has released it yet
        if keypadPressed != -1:
            setAllRows(GPIO.HIGH)
            if GPIO.input(keypadPressed) == 0:
                keypadPressed = -1
            else:
                time.sleep(0.1)
        # Otherwise, just read the input
        else:
            if not commands():
                read(C1, ["1","4","7","*"])
                read(C2, ["2","5","8","0"])
                read(C3, ["3","6","9","#"])
                read(C4, ["A","B","C","D"])
                time.sleep(0.1)
            else:
                time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopped!")