import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
print str(camlist)
cam = pygame.camera.Camera(camlist[0])
cam.start()
img = cam.get_image()
import pygame.image
pygame.image.save(img, "/home/pi/webcam/test.jpg")
pygame.camera.quit()

