from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home page')
def info(request):
    return render(request,'index.html')
def game(request):
    return render(request,'game.html')
def fom(request):
    return render(request,'from.html')
# def test(request):
    