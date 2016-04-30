import os
import datetime
import subprocess
import sys
import socket
import time
import json
from time import mktime
import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects


device_address = "28-00000593e34f" # Change this to your specific value
device_file_name = "/sys/bus/w1/devices/"+ device_address +"/w1_slave"


username = 'ishit.softweb'
api_key = 'h8k7gvirru'
stream_token = 'fyrkvzg0i6'


def read_temperature(device_file):
 # Make sure we have the correct kernel modules loaded
 os.system("/sbin/modprobe w1_gpio")
 os.system("/sbin/modprobe w1_therm")

 temp_file = open(device_file)
 text = temp_file.read().split("\n")
 temp_file.close()
    
 if (len(text) > 0 and text[0].endswith("YES")): # We have some output
  # We have data so grab the last chars of the second line (i.e. the temperature)
  position = text[1].find("t=")
  if (position != -1):
   print position+2
   return int(text[1][-(len(text[1]) - position - 2):])
  else:
   return -100000
 else:
  retun -100000 	


py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = Layout(
    title='Raspberry Pi Streaming Temprature Data'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Temrature Values')


stream = py.Stream(stream_token)
stream.open()

while True:
	 

	 raw_temp = read_temperature(device_file_name)
	 sensorValue = str(round(raw_temp / 1000.0, 1)) 
	 print sensorValue
	 print datetime.datetime.now()
	 sensor_data = sensorValue
	 stream.write({'x': datetime.datetime.now(), 'y': sensor_data})
	 time.sleep(1) # delay between stream posts





