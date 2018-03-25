from firebase import Firebase
f = Firebase('https://satyam-tarp.firebaseio.com/')
f = Firebase('https://satyam-tarp.firebaseio.com/message_list')
r = f.push({'user_id': 'wilma', 'text': 'Hello'})
Name= raw_input("enter your name")
Text=raw_input('enter you message')
r = f.push({'user_id': Name, 'text': Text})
