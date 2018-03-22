from firebase import firebase
firebase = firebase.FirebaseApplication('https://satyam-tarp.firebaseio.com/', None)
result = firebase.get('/users', None)
print result