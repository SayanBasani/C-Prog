from django.http import HttpResponse

def home(request):
    return HttpResponse('Hey i am sayan')
def contact(request):
    return HttpResponse("i am contact page")
def google(request):
    x="https://www.google.com/"
    return HttpResponse(x)