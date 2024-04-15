from django.shortcuts import render,redirect

# Create your views here.
def HomePage(request):
    data = None
    print('data is : ')
    data = request.session.get('data')
    print(data)
    request.session['data']=data
    return render(request,'HomePage.html',{'data':data})
def product(request):
    return render(request , 'product.html')