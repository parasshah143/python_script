import pygame
import pygame.camera
from pygame.locals import *
import pygame.image
import sys
import time
import RPi.GPIO as gpio
#from datetime import date
import datetime

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(37,gpio.IN)
gpio.setup(11,gpio.OUT)

global pygame
global datetime

def motion_detect():
    while True:
	     
             if gpio.input(37)==1:
		gpio.output(11, True)
          	print "Motion Detected"
		pygame.init()
		pygame.camera.init()		
		camlist = pygame.camera.list_cameras()
		print str(camlist)
		cam = pygame.camera.Camera(camlist[0])
		cam.start()
		img = cam.get_image()
		pygame.image.save(img, "/home/pi/webcam/final_"+datetime.datetime.now().ctime()+".jpg")
		pygame.camera.quit()
    	     else: 	
	 	gpio.output(11, False)
                
if __name__ == "__main__":
	try:
		motion_detect()		
	except:
		pass

        	
        
