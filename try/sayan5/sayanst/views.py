from django.shortcuts import render,HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("this is sayan home")
# def about(request):
#     return HttpResponse("this is for about ")
def page(request):
    return render(request,'page.html')