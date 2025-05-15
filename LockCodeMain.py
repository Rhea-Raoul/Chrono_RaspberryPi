# Include the library files
import RPi.GPIO as GPIO
import time
import requests
from keypad import *
from buzzer import *
from lcd import *
from system import *
from relay import *

#Ensuring the LockCodeMain runs only when it is being executed directly
#and not when it is being imported
if __name__ == "__main__":

    #Setting default mode value which is accepting the User's ID
    mode = 1
    
    # Initialize LCD
    # Create an object for the LCD
    main_lcd = init_lcd()

    #Initialzing the keypad, buzzer and relay
    init_keypad()
    init_buzzer()
    init_relay()

    init_System(main_lcd)

#Main system loop
try:
    while True:
        if mode == 1:       
            write_lcd(0, 0, "Enter your ID: ")
            read_input = read_from_keypad()
            
            match read_input:
                case "clear":
                    print("Input reset!")
                    clear_lcd()
                    write_lcd(0, 5, "Clear")
                    time.sleep(1)
                    clear_lcd()
                    read_input = ""

                case "enter":
                    read_input = ""
                    mode += 1
                    time.sleep(0.5)
                    clear_lcd()
                
                #default in case the user's actions don't match any of the cases
                case _:
                    # Writing the userId to the LCD
                    userId = ""
                    userId = read_input
                    write_lcd(1, 0, userId)

        #This mode is used to accept the passcode
        elif mode == 2:     
            write_lcd(0, 0, "Enter your PIN: ")
            read_input = read_from_keypad()

            match read_input:
                case "clear":
                    print("Input reset!")
                    clear_lcd()
                    write_lcd(0, 5, "Clear")
                    time.sleep(1)
                    clear_lcd()
                    read_input = ""
                
                case "enter":
                    read_input = ""
                    mode += 1
                    time.sleep(0.5)
                    clear_lcd()
                    #increment the mode to 3 so as to move on to the validation section

                #default in case which reads user input from the keypad
                #and writes it to the LCD
                case _:
                    # Writing the passcode to the LCD
                    passCode = read_input
                    write_lcd(1, 0, passCode)

        #Code to validate user ID and passcode        
        elif mode == 3:
            #Sending the passcode and ID to the ChronoLock Web Server to validate
            #API endpoint
            url = f"http://172.19.16.54:5000/access_request/{userId}/{passCode}"

            try:
                #A GET request to the API
                response = requests.get(url)
                
                #Print the response
                print(response.status_code)
                print(response.text)
            except requests.exceptions.ConnectionError as e:
                #Print the error if the request fails
                print(f"Connection error!: {e}")

            #Code to be executed if the user ID and passcode were correct
            #and the passcode was not expired
            if response.text == "Access Granted":
                write_lcd(0, 0, "Access Granted")
                time.sleep(0.5)
                clear_lcd()
                write_lcd(0, 0, "Welcome")
                time.sleep(0.5)
                clear_lcd()

                if relayState == False:
                    GPIO.output(Relay, GPIO.HIGH)
                    print("Relay ON")
                    buzzer_beep(0.5)
                    time.sleep(3)
                    relayState = True
                if relayState:
                    GPIO.output(Relay, GPIO.LOW)
                    print("Relay OFF")
                    for _ in range(2):
                        buzzer_beep(0.1)
                    relayState = False
            
            #Code to be executed if either the user ID or passcode was
            #incorrect or if the passcode was expired
            elif response.text == "Access Denied":
                print("Incorrect code")
                clear_lcd()
                write_lcd(0, 1, "Access Denied!")
                time.sleep(0.1)
                for _ in range(3):
                    buzzer_beep(0.3)
                clear_lcd()
            mode = 1
            userId = ""
            passCode = ""
    
except KeyboardInterrupt:
    clear_lcd()
    time.sleep(0.5)
    GPIO.cleanup()
    print("Stopped!")