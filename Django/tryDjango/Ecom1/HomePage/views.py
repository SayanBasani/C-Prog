from django.shortcuts import render

# Create your views here.
def HomePage(request):
    number = range(10)
    return render(request,'HomePage.html',{'number':number})
def nav(request):
    return render(request,"nav.html")
def nav1(request):
    return render(request,"nav1.html")
def product(request):
    return render(request,"Product.html")