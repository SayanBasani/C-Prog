from django.shortcuts import render,redirect
import pyrebase
from django.contrib import messages
from django.http import HttpResponse

firebaseConfig = {
  "apiKey": "AIzaSyChRASyv9NMBjFOTxcUeEHs0caRWbpZ3hE",
  "authDomain": "final-try-4ddcc.firebaseapp.com",
  "projectId": "final-try-4ddcc",
  "storageBucket": "final-try-4ddcc.appspot.com",
  "messagingSenderId": "528992459991",
  "appId": "1:528992459991:web:bab91365d7a2414d796492",
  "measurementId": "G-0SGMFF7R62",
  "databaseURL":"https://final-try-4ddcc-default-rtdb.asia-southeast1.firebasedatabase.app/",
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
Database=firebase.database()

def singin(request):
    print("start for singin ...........................")
    userName = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("pas")
    data = { "userName" : userName , "email" : email , "password" : password }
    try:
        auth.create_user_with_email_and_password(email,password)
        Database.child("users").push(data)
        print("sinin is complit ................................")
        # return redirect('login')
        return render(request,'login.html')
    except Exception as e:
        error_message = str(e)
        if 'INVALID_EMAIL' in error_message:
            error_message = 'Invalid email address.'
        elif 'EMAIL_EXISTS' in error_message:
            error_message = 'Email address already exists.'
        messages.error(request, error_message)
        
        
    return render(request,'signup.html')



    # return render(request,'signup.html')
# Create your views here.
def login(request):
    print("login start ..............................")
    userName = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("pas")
    # data = { "userName" : userName , "email" : email , "password" : password }
    try:
        auth.sign_in_with_email_and_password(email,password)
        # Database.child("users").push(data)
        print("SUCCES FULL LOGIN ")
        print("login complit ..............................")

        return render(request,'succes.html',{"email":email})
    except Exception as e:
        print("TRY AGAIN")
        messages.error(request, 'Succes full login')
    return render(request,'login.html')
    

    
def suc(request):
    return render(request,'succes.html')
def home(request):
    return render(request,'home.html')
    
    
    
# def login(request):
#     userName = request.POST.get("name")
#     email = request.POST.get("email")
#     password = request.POST.get("pas")
#     data = { "userName" : userName , "email" : email , "password" : password }
#     try:
#         auth.create_user_with_email_and_password(email,password)
#         Database.child("users").push(data)
#         return redirect('login')
#     except:
#         print("TRY AGAIN")
#         return render(request,'sinup.html')
#     return render(request,'login.html')
    
# def singin(request):
#     userName = request.POST.get("name")
#     email = request.POST.get("email")
#     password = request.POST.get("pas")
#     data = { "userName" : userName , "email" : email , "password" : password }
#     try:
#         auth.create_user_with_email_and_password(email,password)
#         Database.child("users").push(data)
#         return redirect('login')
#     except:
#         print("TRY AGAIN")
#         return render(request,'sinup.html')
#     # return render(request,'signup.html')
