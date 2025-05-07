# Include the library files
import RPi.GPIO as GPIO
import time
import requests
from keypad import init_keypad, read, checkSpecialKeys, setAllRows
from keypad import keypadPressed, C1, C2, C3, C4, R1, R2, R3, R4
from buzzer import *
from lcd import *
from system import *
from relay import *


if __name__ == "__main__":

    userId = ""
    passCode = ""

    mode = 1

    # Initialize LCD
    # Create an object for the LCD
    main_lcd = init_lcd()

    init_keypad()
    init_buzzer()
    init_relay()

    init_System(main_lcd)




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
                #write_lcd(0, 0, "Enter your ID: ")

                            
                if keypadPressed != -1:
                    print("Keypad pressed: ", keypadPressed)
                    setAllRows(GPIO.HIGH)
                    print("Keypad pressed: ", keypadPressed)
                    read_key = GPIO.input(keypadPressed)
                    if read_key == 0:

                        keypadPressed = -1

                    else:
                        time.sleep(0.2)
                else:
                    if not checkSpecialKeys():
                        userId = read(C1, ["1","4","7","*"])
                        userId = read(C2, ["2","5","8","0"])
                        userId = read(C3, ["3","6","9","#"])
                        userId = read(C4, ["A","B","C","D"])


            #elif mode == 2:
                #write_lcd(0, 0, "Enter your PIN: ")
            
            time.sleep(0.2)
            
    except KeyboardInterrupt:
        clear_lcd()
        GPIO.cleanup()
        print("Stopped!")

