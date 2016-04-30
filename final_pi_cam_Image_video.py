import picamera
import time
from time import sleep
import sys
import RPi.GPIO as gpio
#from datetime import date
import datetime

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(37,gpio.IN)
gpio.setup(11,gpio.OUT)

global datetime

def motion_detect():
    while True:
	     
             if gpio.input(37)==1:
		gpio.output(11, True)
          	print "Motion Detected"

		with picamera.PiCamera() as camera:
		    camera.start_preview()
		    camera.start_recording("/var/www/picamera/video_"+time.strftime("%Y%m%d_%H%M%S", time.gmtime())+".h264")
		    sleep(2)
		    camera.stop_recording()
		    camera.stop_preview()

    	     else: 	
	 	gpio.output(11, False)
                
if __name__ == "__main__":
	try:
		motion_detect()		
	except:
		pass
