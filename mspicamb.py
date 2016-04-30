import os
from datetime import datetime
import sys
import azure
from azure.storage import BlobService
import socket
import time
import RPi.GPIO as gpio
from time import mktime
import io
import picamera
import base64
from base64 import decodestring


gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(37, gpio.IN)
from uuid import getnode as get_mac

mac = get_mac()
# print mac 
from azure.servicebus import (
  _service_bus_error_handler
  )
 
from azure.servicebus.servicebusservice import (
  ServiceBusService,
  ServiceBusSASAuthentication
  )
 
from azure.http import (
  HTTPRequest,
  HTTPError
  )
 
from azure.http.httpclient import _HTTPClient

from azure.http.httpclient import _HTTPClient


class EventHubClient(object):
 
  def sendMessage(self,body,partition):
    eventHubHost = "softwebiot.servicebus.windows.net"
 
    httpclient = _HTTPClient(service_instance=self)
 
    sasKeyName = "sendrule"
    sasKeyValue = "wu3y8i2FyDj9SyDbUg4XhaUfF4Jlk/IC31etmHTEtnw="
 
    authentication = ServiceBusSASAuthentication(sasKeyName,sasKeyValue)
 
    request = HTTPRequest()
    request.method = "POST"
    request.host = eventHubHost
    request.protocol_override = "https"
    request.path = "/sensordata/publishers/" + partition + "/messages?api-version=2014-05"
    request.body = body
    request.headers.append(('Content-Type', 'application/atom+xml;type=entry;charset=utf-8'))
 
    authentication.sign_request(request, httpclient)
 
    request.headers.append(('Content-Length', str(len(request.body))))
 
    status = 0
 
    try:
        resp = httpclient.perform_request(request)
        status = resp.status
    except HTTPError as ex:
        status = ex.status
 
    return status

global time

def motion_detect():
    try:
        while True:
            if gpio.input(37) == 1: 
            	    print "Motion Detected"
                    hubClient = EventHubClient()
                    hostname = socket.gethostname()
    
                    host = socket.gethostname()
                    body = ""
                    first = True
                    sensorType = "Motion"
                    sensorValue = "1"
                    sensorId = 'Motion@1stfloor'
                    tablename = 'sensordata'
                    motiontime = time.strftime('%m/%d/%Y %H:%M:%S');
                    add_info = host + "_PiCam@1stfloor_" + motiontime.replace("/","-").replace(" ","-").replace(":","-") + ".jpg"
                    print motiontime
                    
                    if first == True:
                        first = False
                    else:    
                    	body += ","
                    
                    #deviceid_sensorid_motiondatetime (- replace with).png
                    
                    body += "{ \"DeviceId\" : \"" + host + "\", \"SensorId\" : \"" + sensorId + "\", \"SensorType\" : \"" + sensorType + "\", \"SensorValue\" : \"" + sensorValue + "\", \"Datetime\" : \"" + motiontime + "\", \"AdditionalInfo\" : \"" + add_info + "\", \"table_name\" : \"" + tablename + "\" }"
                    
    
                    my_stream = io.BytesIO()
                    with picamera.PiCamera() as camera:
                        camera.resolution = (640, 480)
                        camera.capture(my_stream, 'jpeg')
                        img_stream = base64.b64encode(my_stream.getvalue())
                        img_type = "jpeg"
                        sensorType = "PiCam"
                        sensorValue = img_stream
                        sensorId = 'PiCam@1stfloor'
                        #add_info = host + "_" + sensorId + "_" + motiontime.replace("/","-").replace(" ","-").replace(":","-") + ".jpg"
                    print add_info
                    print  time.strftime('%m/%d/%Y %H:%M:%S')    
                    cbody = "{ \"DeviceId\" : \"" + host + "\", \"SensorId\" : \"" + sensorId + "\", \"SensorType\" : \"" + sensorType + "\", \"SensorValue\" : \"" + sensorValue + "\", \"Datetime\" : \"" + time.strftime('%m/%d/%Y %H:%M:%S') + "\", \"AdditionalInfo\" : \"" + add_info + "\", \"table_name\" : \"" + tablename + "\" }"
                    hubStatus = hubClient.sendMessage(body, hostname)
                    print hubStatus
                    hubStatus = hubClient.sendMessage(cbody, hostname)
                    print hubStatus
                    print  time.strftime('%m/%d/%Y %H:%M:%S')
                    #print cbody
                    
                    upload = my_stream.getvalue();
		    container = "motioncaptureimages-direct"; 
		    blob = add_info;
		    blob_service = BlobService(account_name='commoniotstorage', account_key='PX4BC7LHPFWYtayYDtHAC/CV/+VHWOudqXBB9En2dGYHg3yGnXwbXIOHyvdq0gEU0P4FTV0A5AlRBHFe5DL5Kg==')
		    blobstatus = blob_service.put_block_blob_from_bytes(
			        	container,
				        blob,
			        	upload,
			        	x_ms_blob_content_type='image/jpg'
	    			)
	    
		    print blobstatus
		    print  time.strftime('%m/%d/%Y %H:%M:%S')
		    
		    
                    
    except KeyboardInterrupt:
        gpio.cleanup()
        print "\n Terminated by User"
        sys.exit()


if __name__ == "__main__": motion_detect()



