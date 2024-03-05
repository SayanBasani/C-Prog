from django.shortcuts import render

# Create your views here.
def HomePage(request):
    number = range(10);
    return render(request,'HomePage.html',{'number':number})