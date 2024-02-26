from django.shortcuts import render,HttpResponse
import pyrebase


config = {
  "apiKey": "AIzaSyAitRioRAwvLZToKjdO-REqdYqpDtilVC8",
  "authDomain": "usingpyerbase.firebaseapp.com",
  "projectId": "usingpyerbase",
  "storageBucket": "usingpyerbase.appspot.com",
  "messagingSenderId": "765481551563",
  "appId": "1:765481551563:web:ff79d829d1e7d5b56efd4e",
  "measurementId": "G-5KVC4R561Y",
  "databaseURL":"https://usingpyerbase-default-rtdb.asia-southeast1.firebasedatabase.app/",
}

fierbase = pyrebase.initialize_app(config)
auth = fierbase.auth()

def singin(request):
    return render(request,"singin.html")
def postsigin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=auth.sign_in_with_email_and_password(email,password)
    return render(request,"info.html",{"e":email})
# Create your views here.
# def index(request):
#     return HttpResponse("this is sayan home")
# def about(request):
#     return HttpResponse("this is for about ")
def page(request):
    return render(request,'page.html')