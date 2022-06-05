#importing libraries
import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep
import smbus
import requests
DEVICE = 0x23
RES = 0x20
bus = smbus.SMBus(1)

#posts an HTTP request to Webhook
def light():
    requests.post('https://maker.ifttt.com/trigger/light/with/key/b2KC93lYIFpBaCZ0hOnhQz', params={"value1":"none","value2":"none","value3":"none"})

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

##pin setup
GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(18,500)
servo.start(0)

try:
    #stores previous light reading
    prevdata = 0
    while True:
        data = bus.read_i2c_block_data(DEVICE, RES)
        data = int((data[0] << 8) + data[1])
        print(data)
        #if current light level > threshold and previous < threshold
        if data > 500 and prevdata < 500:
            level = 'Too bright. Activating Servo'
            light()
            for dc in range(50,101,5):
                servo.ChangeDutyCycle(dc)
                sleep(0.5)
          
        #if light is now dark below threshold
        if data < 500 and prevdata > 500:
            print('Deactivating servo')
            for dc in range(100,49,-5):
                servo.ChangeDutyCycle(dc)
                sleep(0.5)            
        
        elif data < 500:
            level = 'Too dark'

        print(level)
        prevdata = data #update light reading
        sleep(5)
        
except KeyboardInterrupt:
    print("Program stopped")