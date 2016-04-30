import sys
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(37,gpio.IN)
gpio.setup(11,gpio.OUT)

def motion_detect():
    while True:
	     
             if gpio.input(37)==1:
		gpio.output(11, True)
                print "Motion Detected"
    	     else: 	
	 	gpio.output(11, False)
                
if __name__ == "__main__":
    motion_detect()

        	
        
