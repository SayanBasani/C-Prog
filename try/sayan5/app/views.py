from django.shortcuts import render
import pyrebase 
from firebase import Firebase
import firebase_admin as pyrebase
from firebase_admin import credentials

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
# firebase = Firebase(config)
auth = firebase.database()


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

def login(request):
    if request.method == "POST":
        email =request.POST['email']
        password = request.POST['password']
        auth.push()

# views.py
# config ={
#     "apiKey": "AIzaSyD-qrPzPuJvGyDB186fzBx6S2XloJ4eX0g",
#     "authDomain": "try1-4b852.firebaseapp.com",
#     "projectId": "try1-4b852",
#     "storageBucket": "try1-4b852.appspot.com",
#     "messagingSenderId": "1095348043052",
#     "appId": "1:1095348043052:web:8dd19d6de705fb6bcb0089",
#     "measurementId": "G-6L1EYXQKQG",
#     "databaseURL": "https://try1-4b852-default-rtdb.firebaseio.com/",
# }
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from firebase import firebase

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         # Authenticate with Firebase
#         firebase_auth = firebase.FirebaseApplication('https://try1-4b852-default-rtdb.firebaseio.com/', None)
#         user_data = firebase_auth.get('/users', None)

#         if user_data and email in user_data and user_data[email]['password'] == password:
#             user = authenticate(request, username=email, password=password)

#             if user:
#                 login(request, user)
#                 messages.success(request, 'Login successful.')
#                 return redirect('home')  # Redirect to your home page
#             else:
#                 messages.error(request, 'Invalid login credentials.')
#         else:
#             messages.error(request, 'Invalid login credentials.')

#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'Logout successful.')
#     return redirect('login')  # Redirect to your login page




# from django.shortcuts import render
# from firebase import firebase

# def sinin(request):
#     return render(request,'fill.html')

