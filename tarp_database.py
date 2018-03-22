import serial
import time
import requests
import json
import serial


import csv
firebase_url = 'https://satyam-tarp.firebaseio.com/'
#Connect to Serial Port for communication
## ser = serial.Serial('COM15', 9600, timeout=0)
s=serial.Serial("/dev/ttyACM0",9600)
#Setup a loop to send Temperature values at fixed intervals
#in seconds
fixed_interval = 10

         
    
    
    


while 1:
       temperature_c= s.readline()
       for name in s.readline().split(): 
           if (name[0:6]== "Amount"):
      
              print "hi"
      #current time and date
	   time_hhmmss = time.strftime('%H:%M:%S')
	   date_mmddyyyy = time.strftime('%d/%m/%Y')
	    
	    #current location name
	   temperature_location = 'Mumbai-Kandivali';
	   print temperature_c + ',' + time_hhmmss + ',' + date_mmddyyyy + ',' + temperature_location
	    
	    #insert record
	   data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':temperature_c}
	   result = requests.post(firebase_url + '/' + temperature_location + '/temperature.json', data=json.dumps(data))
	    
	   print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
	   time.sleep(fixed_interval)
	 

      
