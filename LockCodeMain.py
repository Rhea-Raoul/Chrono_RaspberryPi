# Include the library files
import RPi.GPIO as GPIO
import time
import requests
from keypad import init_keypad, keypadCallback
from buzzer import init_buzzer, buzzer_beep
from lcd import *
from system import init_System
from relay import init_relay

# Initialize LCD
# Create an object for the LCD
main_lcd = init_lcd()

init_keypad()
init_buzzer()
init_relay()

init_System(main_lcd)

# The GPIO pin of the column of the key that is currently
# being held down or -1 if no key is pressed
keypadPressed_id = -1
keypadPressed_code = -1
# Enter your PIN
user_id = ""
secretCode = "1234"
correct_id = "12"
input = ""
mode = 1

'''
def commands():
    global relayState
    global input
    global user_id
    global mode
    clear_pressed = False
    GPIO.output(C4, GPIO.HIGH)
    
    # Clear PIN 
    if (GPIO.input(R3) == 1 ):
        print("Input reset!");
        lcd.clear()
        lcd.cursor_pos = (0, 5)
        lcd.write_string("Clear")
        time.sleep(1)
        clear_pressed = True
    GPIO.output(C4, GPIO.HIGH)

    # Check PIN
    if (not clear_pressed and GPIO.input(R4) == 1):
        if mode == 1 and user_id != "":
            lcd.clear()
            lcd.cursor_pos = (0, 3)
            lcd.write_string("Enter Your PIN")
            mode = 2
            input = ""
        elif mode == 2:
            if input == secretCode and user_id == correct_id:
                lcd.clear()
                lcd.cursor_pos = (0, 3)
                lcd.write_string("Successful")
                
                if relayState == False:
                    GPIO.output(Relay,GPIO.HIGH)
                    buzzer_beep(0.5)
                    relayState = True
                    
                if relayState:
                    GPIO.output(Relay,GPIO.LOW)
                    buzzer_beep(0.1)
                    buzzer_beep(0.1)
                    relayState = False
                    
                
            else:
                print("Incorrect code!")
                lcd.clear()
                lcd.cursor_pos = (0, 3)
                lcd.write_string("Wrong PIN!")
                time.sleep(0.5)
                buzzer_beep(0.3)
                buzzer_beep(0.3)
                buzzer_beep(0.3)
            clear_pressed = True
    GPIO.output(C1, GPIO.LOW)
    if clear_pressed:
        input = ""
        user_id = ""
        mode = 1
    return clear_pressed

'''


try:
    while True:
        if mode == 1:       
            write_lcd(0, 0, "Enter your ID: ")

        elif mode == 2:
            write_lcd(0, 0, "Enter your PIN: ")
        
        
        
        
        
        
        time.sleep(0.1)

except KeyboardInterrupt:
    clear_lcd()

    print("Stopped!")



'''
    if mode == 1:       
        write_lcd(0, 0, "Enter your ID: ")
        if keypadPressed_id != -1:
            setAllRows(GPIO.HIGH)
            if GPIO.input(keypadPressed_id) == 0:
                keypadPressed_id = -1
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
            mode += 1
    elif mode == 2:
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Enter your PIN: ")
        if keypadPressed_code != -1:
            setAllRows(GPIO.HIGH)
            if GPIO.input(keypadPressed_code) == 0:
                keypadPressed_code = -1
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
    mode = 1
    time.sleep(0.1)

'''