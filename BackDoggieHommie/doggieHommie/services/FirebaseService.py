import pyrebase


firebaseConfig = {

  "apiKey": "AIzaSyCclOOJ1xqH6pPTe9cJ_ICmoGqm8I5WLbM",
  "authDomain": "doggiehommie.firebaseapp.com",
  "databaseURL": "https://doggiehommie-default-rtdb.firebaseio.com",
  "projectId": "doggiehommie",
  "storageBucket": "doggiehommie.appspot.com",
  "messagingSenderId": "261053155965",
  "appId": "1:261053155965:web:ec6ad2ff3ae4bffe60ff14",
  "measurementId": "G-ES2XFZ01MQ"

}
firebase = pyrebase.initialize_app(firebaseConfig)