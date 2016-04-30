import os
from datetime import datetime
import sys
import azure
import socket
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(37,gpio.IN)

from uuid import getnode as get_mac
mac = get_mac()

#print mac

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

class EventHubClient(object):
 
  def sendMessage(self,body,partition):
    eventHubHost = "softwebiot.servicebus.windows.net"
 
    httpclient = _HTTPClient(service_instance=self)
 
    sasKeyName = "sendrule"
    sasKeyValue = "5ZWZQipiXZrZ4oYatHcLE7KXkyASZ6EbFoM4NSjSkLc="
 
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
class EventDataParser(object):
 
  # def getMessage(self):
  #   body = "1"
 
  #   return body

  def motion_detect():
    try:
        while True:
            if gpio.input(37)==1:
                print "Motion Detected"    
                hubClient = EventHubClient()
                parser = EventDataParser()
                hostname = socket.gethostname()
                #sensor = sys.argv[2]
                 
                body = "1"
                hubStatus = hubClient.sendMessage(body,hostname)
                # return the HTTP status to the caller
                print hubStatus
                print hostname            
    except KeyboardInterrupt:
        gpio.cleanup()
        print "\n Terminated by User"
        sys.exit()


if __name__ == "__main__":
    motion_detect()