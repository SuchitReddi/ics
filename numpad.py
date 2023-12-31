import RPi.GPIO as GPIO
import time
import os
import sys

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

# Hides long error tracebacks. Comment out if you want to find error causes.
sys.tracebacklimit=0

# The GPIO pin of the column of the key that is being held down or -1 if no key is pressed
keypadPressed = -1

print("Please enter your code")
secretCode = "7897"
#input = ""
input = "8888"
# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Use the internal pull-down resistors
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# This callback registers the key that was if no other key is currently pressed
def keypadCallback(channel):
    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel

# Detect the rising edges on the column lines of the keypad.
# This way, we can detect if the user a button when we send a pulse.
GPIO.add_event_detect(C1, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C2, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C3, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C4, GPIO.RISING, callback=keypadCallback)

# Sets all lines to a specific state. This is for detecting when the user releases a button
def setAllLines(state):
    GPIO.output(L1, state)
    GPIO.output(L2, state)
    GPIO.output(L3, state)
    GPIO.output(L4, state)

# reads the columns and appends the value, that corresponds
# to the button, to a variable
def readLine(line, characters):
    global input
    # We have to send a pulse on each line to
    # detect button presses
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        input = input + characters[0]; print(input)
    if(GPIO.input(C2) == 1):
        input = input + characters[1]; print(input)
    if(GPIO.input(C3) == 1):
        input = input + characters[2]; print(input)
    if(GPIO.input(C4) == 1):
        input = input + characters[3]; print(input)
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        # If a button was previously pressed,
        # check, whether the user has released it yet
        if keypadPressed != -1:
            setAllLines(GPIO.HIGH)
            if GPIO.input(keypadPressed) == 0:
                keypadPressed = -1
            else:
                time.sleep(0.1)
        # Otherwise, just read the input
        else:
             if len(input) != len(secretCode):
                readLine(L1, ["1","2","3","A"])
                readLine(L2, ["4","5","6","B"])
                readLine(L3, ["7","8","9","C"])
                readLine(L4, ["*","0","#","D"])
                time.sleep(0.1)
             else:
                 if input == secretCode :
                     print("Correct");
                     input=""
                 else:
                     print("Incorrect!!");
                     input="";
                     os.system("mkdir img")
                     os.system("libcamera-jpeg -o ./img/intruder_captured.jpeg --vflip=1");
                     os.system("convert -resize 10% ./img/intruder_captured.jpeg ./img/intruder_compressed.jpeg");
                     print("Redirecting to send.py"); os.system("venv/bin/python3 send.py") #Anything after this doesn't get executed
    #Clear the list for next time.
except KeyboardInterrupt:
    print("\nApplication stopped!")
