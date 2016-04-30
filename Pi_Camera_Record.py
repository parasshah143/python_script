import time
import picamera
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
   		     #camera.start_preview()
		     #camera.vflip = True
		     #camera.hflip = True
		     camera.brightness = 60
		     time.sleep(2)
    		     camera.capture("/var/www/picamera/image_"+datetime.datetime.now().ctime()+".jpg")
		     camera.start_recording("/var/www/picamera/video_"+time.strftime("%Y%m%d_%H%M%S", time.gmtime())+".h264")	
		     #camera.start_recording("/var/www/picamera/video_"+datetime.datetime.now().ctime()+".mp4")
		     #sleep(30)
		     camera.stop_recording()
                     #camera.stop_preview()		
    	     else: 	
	 	gpio.output(11, False)
                
if __name__ == "__main__":
	try:
		motion_detect()		
	except:
		pass

