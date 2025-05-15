# Chrono_RaspberryPi
This repository contains the code which will control the locking mechanism built using the Raspberry Pi 4 Model B and it's various hardware components.

Documentation:

buzzer.py:
This file controls the buzzer. It contains two functions, "init_buzzer" and "buzzer_beep". The first function is responsible for initializing the buzzer ensuring that it is ready for use when the function is imported in the main file. The buzzer_beep function is simply used to beep the buzzer once and the duration of the delay is defined by the user.

lcd.py:
This file controls the LCD. It contains the "init_lcd" function which intializes as well as creates an lcd object to control the LCD. It also has a "write_lcd" function and "clear_lcd" function which are used to write to and clear the LCD respectively.

keypad.py:
This file controls the keypad. It contains a series of functions and initializations all of which enable the keypad to accept input from the user. The init_keypad function sets the column pins as output pins and the row pins as input pins. Event detection is added to the row pins such that when they're pressed the keypadCallback function is called and the channel of the key pressed is assigned to the "keypadPressed" variable. The keypadCallback function registers the channel of the key pressed. The "read" function is used to determine which combination of row and column pin was pressed, then assigns the corresponding character to the "res" variable. The "is_clear_key_pressed" function and "is_enter_key_pressed" function determine whether the clear or enter key was pressed. The "read_from_keypad" function is used to determine which of the key or keys is being pressed, then return the correct value; if the enter key was pressed then "enter" is returned, if the clear key was pressed then "clear" is returned and if none of those keys were pressed then the user input is read from the keypad and the input variable, with the user input, is returned.

MainLockCode.py:
This is the main code and it is used to accept the user ID and passcode from the user, transmit them to the server using HTTP requests, and then either unlock the lock or keep it locked based on the server's response. All functions from the other files are imported in this code as it's the main script controlling the lock. The default mode, which is the User ID mode, is set and all components are initialized using their initialization functions. The system loading message is displayed on the LCD using the main_lcd variable and init_System function. A continous loop is used to execute the main body of code and the user is prompted for their user ID and passcode. When entered, a GET request is sent to the ChronoLock Web server, with the userId and passCode variables as parameters. Based on whether the User ID and passcode are correct, as well as if the passcode is expired or not, either "Access Granted" or "Access Denied" will be transmitted to the Raspberry Pi from the server. If the response is access granted, the code displays "Access Granted" and "Welcome" on the LCD and the relay is set to high, deactivating the solenoid, and the buzzer beeps once. A short time elapses and the relay is set back to low, reactivating the solenoid and the buzzer beeps twice. If the response is access denied, then the LCD displayes "Access Denied!" and the buzzer beeps three times and the solenoid remains energized.

relay.py:
This file controls the relay, setting the pin number, as well as the relay state.

system.py:
This file is used to set the pin numbering mode and the GPIO warning mode to false. It also includes the start message for when the main code is executed for the first time.
