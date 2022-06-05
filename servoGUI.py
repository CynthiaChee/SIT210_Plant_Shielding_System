#import libraries
from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
from time import sleep
import requests

#setup board and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(18,500)
servo.start(0)

#create window
win = Tk()
win.title("Servo Control")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

#posts HTTP requests to Webhook
def act_msg():
    requests.post('https://maker.ifttt.com/trigger/act_msg/with/key/b2KC93lYIFpBaCZ0hOnhQz', params={"value1":"none","value2":"none","value3":"none"})

def deact_msg():
    requests.post('https://maker.ifttt.com/trigger/deact_msg/with/key/b2KC93lYIFpBaCZ0hOnhQz', params={"value1":"none","value2":"none","value3":"none"})

#activates servo manually
def activate():
    act_msg()
    for dc in range(50,101,5):
        servo.ChangeDutyCycle(dc)
        sleep(0.5)

#deactivates servo manually
def deactivate():
    deact_msg()
    for dc in range(100,49,-5):
        servo.ChangeDutyCycle(dc)
        sleep(0.5)

#closes window
def close():
    win.destroy()

#Buttons
activateButton = Button(win, text = "Activate Servo", font = myFont, command = activate, bg = 'green', height = 1, width = 24)
deactivateButton = Button(win, text = "Deactivate Servo", font = myFont, command = deactivate, bg = 'grey', height = 1, width = 24)
exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = 'blue', height = 1, width = 24)

activateButton.grid(row = 0,column = 1)
deactivateButton.grid(row = 1, column = 1)
exitButton.grid(row = 2, column = 1)