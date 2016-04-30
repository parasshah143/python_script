import os
from datetime import datetime
import subprocess

device_address = "28-00000593e34f" # Change this to your specific value
device_file_name = "/sys/bus/w1/devices/"+ device_address +"/w1_slave"

#flow_x = '{"SensorId": "555555", "SensorType": "Temperature", "SensorValue": "38", "datetime": "05/04/2015"}'

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

raw_temp = read_temperature(device_file_name)
subprocess.call(['curl', '-X', 'POST', '-H', 'Authorization:SharedAccessSignature sr=https://softwebiot.servicebus.windows.net/ioteventhub/publishers%2Fdevice444%2Fmessages&sig=EVQaYY0EkVuW8Kg/eJ1AtZVqxhsRj5FmS0mXRKgKh8k=%3D&se=6523163836&skn=RootManageSharedAccessKey', '-d', 'kkk', 'https://softwebiot.servicebus.windows.net/ioteventhub/publishers/device444/messages'])
print "   Raw temp: ", raw_temp
print "Temperature: ", round(raw_temp / 1000.0, 1)

