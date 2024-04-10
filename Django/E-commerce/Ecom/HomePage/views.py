from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request,'HomePage.html')
def product(request):
    return render(request , 'product.html')