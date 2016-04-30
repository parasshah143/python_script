import os
import datetime
import sys
import time
import io 
import picamera
#import base64 
#from base64 import decodestring
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(37,gpio.IN)

         
                
my_stream = io.BytesIO()
with picamera.PiCamera() as camera:
    #camera.start_preview()
    #time.sleep(2) 
    #camera.resolution = (640, 480) 
    camera.capture(my_stream, 'jpg') 
    #img_stream = base64.b64encode(my_stream.getvalue()) 
    #img_type="jpg" 
    #sensorType = "PiCam" 
    #sensorValue = img_stream 
    #sensorId = 'PiCam@1stfloor' 
    #print sensorValue		        
    #print time.strftime('%m/%d/%Y %H:%M:%S')
		       

#import io
#import time
#import picamera

# Create an in-memory stream
#my_stream = io.BytesIO()
#with picamera.PiCamera() as camera:
    #camera.start_preview()
    # Camera warm-up time
    #time.sleep(2)
    #camera.capture(my_stream, 'jpeg')

