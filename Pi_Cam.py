import picamera
import time
from time import sleep


with picamera.PiCamera() as camera:
    camera.start_preview()
    #camera.start_recording('video.h264')
    camera.start_recording("/var/www/picamera/video_"+time.strftime("%Y%m%d_%H%M%S", time.gmtime())+".h264")
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
