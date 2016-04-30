import sys
import time
import RPi.GPIO as gpio
import subprocess

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(37,gpio.IN)

#flow_x = '{"id_wasp": "111111", "id_secret": "222222", "sensor": "Motion", "value": "2222", "datetime": "05/04/2015"}'

def motion_detect():
    try:
        while True:
            if gpio.input(37)==1:
                print "Motion Detected"
                #subprocess.call(['curl', '-X', 'POST', '-H', 'Authorization:SharedAccessSignature sr=https://softwebiot.servicebus.windows.net/sensordata/publishers%2F202481599737206%2Fmessages&sig=5ZWZQipiXZrZ4oYatHcLE7KXkyASZ6EbFoM4NSjSkLc=%3D&se=6523163836&skn=sendrule', '-d', '1', 'https://softwebiot.servicebus.windows.net/sensordata/publishers/202481599737206/messages'])
    except KeyboardInterrupt:
        gpio.cleanup()
        print "\n Terminated by User"
        sys.exit()


if __name__ == "__main__":
    motion_detect()

