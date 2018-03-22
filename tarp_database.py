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
#Setup a loop to send parking values at fixed intervals
#in seconds
fixed_interval = 10

         
    
    
    


while 1:
       parking_c= s.readline()
       print s.readline().split()
       for name in s.readline().split(): 
       	   
           if (name.find("Amount")):
      
              print "hi"
      #current time and date
	   time_hhmmss = time.strftime('%H:%M:%S')
	   date_mmddyyyy = time.strftime('%d/%m/%Y')
	    
	    #current location name
	   parking_location = 'Vellore';
	   print parking_c + ',' + time_hhmmss + ',' + date_mmddyyyy + ',' + parking_location
	    
	    #insert record
	   data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':parking_c}
	   result = requests.post(firebase_url + '/' + parking_location + '/parking.json', data=json.dumps(data))
	    
	   print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
	   
	 

      
