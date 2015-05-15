#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import picamera
from datetime import datetime
 
# Turn off GPIO warnings
GPIO.setwarnings(False)

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)
 
# Set GPIO for camera LED
# Use 5 for Model A/B and 32 for Model B+
CAMLED = 32
 
# Set GPIO to output
GPIO.setup(CAMLED, GPIO.OUT, initial=False) 
 
# Five iterations with half a second
# between on and off
for i in range(5):
 GPIO.output(CAMLED,True) # On
 with picamera.PiCamera() as camera:
	camera.capture('IMG_' + datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg', format='jpeg')
	pass
# time.sleep(0.5)
 GPIO.output(CAMLED,False) # Off
 time.sleep(1)

