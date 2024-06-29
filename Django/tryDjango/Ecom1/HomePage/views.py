from django.shortcuts import render
from django.http import JsonResponse

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
def ok(request):
    abc={
        'name':1,'a':2,
    }
    return render(request,"ok.html",{'abc':abc})
def oks(request):
    okdata = {
        "name":"sayan",
        "age":20, 
    }
    return JsonResponse(okdata)