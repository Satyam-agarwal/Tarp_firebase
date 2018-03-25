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
       parking_c1= s.readline()
       parking_c2= s.readline()
       
       
      
    
       time_hhmmss = time.strftime('%H:%M:%S')
       date_mmddyyyy = time.strftime('%d/%m/%Y')
	    
	    #current location name
       parking_location = 'Vellore';
       print parking_c + ',' + time_hhmmss + ',' + date_mmddyyyy + ',' + parking_location
	    
       	    #insert record
       data = {'time':time_hhmmss,'Slot2':parking_c[11:],"Slot3":parking_c1[11:],"Slot1":parking_c2[11:]}
       result = requests.post(firebase_url + '/' + parking_location + '/parking.json', data=json.dumps(data))
       time.sleep(10)	    
       print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
	   
	 

      
