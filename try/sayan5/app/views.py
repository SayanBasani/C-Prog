from django.shortcuts import render
import pyrebase 
# import firebase_admin as pyrebase
# from firebase_admin import credentials

config ={
    "apiKey": "AIzaSyD-qrPzPuJvGyDB186fzBx6S2XloJ4eX0g",
    "authDomain": "try1-4b852.firebaseapp.com",
    "projectId": "try1-4b852",
    "storageBucket": "try1-4b852.appspot.com",
    "messagingSenderId": "1095348043052",
    "appId": "1:1095348043052:web:8dd19d6de705fb6bcb0089",
    "measurementId": "G-6L1EYXQKQG",
    "databaseURL": "https://try1-4b852-default-rtdb.firebaseio.com/",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def test(request):
    email=request.POST.get('email')
    password = request.POST.get('password')
    print(f'User email:- {email} \n password :- {password}')
    auth(email,password)
    return render(request,'Home.html')
def auth(email,password):
    auth=firebase.auth()
    auth.create_user_with_email_and_password(email, password)
    auth.send_email_verification(user['idToken'])

















def sinin(request):
    return render(request,'fill.html')
def home(request):
    return render(request,'Home.html')
def i(request):
    return render(request,'info.html'),
def p(request):
    return render(request,'page.html'),