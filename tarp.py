
import serial


import csv
s=serial.Serial("/dev/ttyACM1",9600)
while 1:
      print s.readline().split()
      for name in s.readline().split(): 
          
          if (name[0:6]== "Amount"):
      
             print "hi"
 
      with open('example5.csv', 'w') as csvfile:
	   fieldnames = ['first_name', 'last_name', 'Grade']
	   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	 
	   writer.writeheader()
	   writer.writerows([{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'},
		             {'Grade': 'A', 'first_name': 'Rachael',
		                 'last_name': 'Rodriguez'},
		             {'Grade': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
		             {'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
		             {'Grade': 'A', 'first_name': 'Kennzy', 'last_name': 'Tim'}])
 
print("writing complete")
