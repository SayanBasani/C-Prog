from django.shortcuts import render,redirect
from django.urls import reverse
import firebase,pyrebase,firebase_admin
from firebase_admin import credentials , firestore
import json
firebaseConfig = {
  "apiKey": "AIzaSyA1l6YTxtr8Xx7KcdPytaKs2YsGblMMNJk",
  "authDomain": "e-commers-web-page.firebaseapp.com",
  "projectId": "e-commers-web-page",
  "storageBucket": "e-commers-web-page.appspot.com",
  "messagingSenderId": "620595830414",
  "appId": "1:620595830414:web:9456fb464b28906f7d73df",
  "measurementId": "G-XQFMT37DGZ",
  "databaseURL":" "
}
service={
  "type": "service_account",
  "project_id": "e-commers-web-page",
  "private_key_id": "cd7097f68e100d1f20e677f5d52d434852f1fd8e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDUvkUac1UUrBwm\nqxjLN8boYw6mJNKscNvC1uQ3ZWgzw2tabLKeWjHGJFULaJFocRqc3qi90qI4OG0u\n7ejg/UJFz05GrWHo/+J4+RoHH2Y0aO1CoOIawzW3ar5bbU0YUiDI5f1XG7doU/1t\nbhVZlcYTjoCEtHyepZO8hU4wIVGycp1x+uenrQO5geYWBeNAiLB4udTkOeaiA6HE\nK5X8gVY87OYJldzQSSB2PiwFczMYwShvuS/+qi2IjhxBjUapFLGyr64BGfDWWAll\nki/PQE6Ex+oqXQBYHk/1Zn9YUkh13H1UFWKfhoVh7GH2FBgLs5kefoCh5aasdJIA\nFSQ2vrxdAgMBAAECggEABlpMK/cHsl9VU95GFkNrICNdG57734RbO505IWJY0zrh\nqMiYKNxeoiERnQ6ZUPoXplmLxmdUysL8l6spChbl9Lm1B61DwDZr59rgaRgJ8ES1\n2Qh+1/e+UeTRHF/OLoy9R+J+RyyftHDVn3/rCUrMqGbX9Z6CHiapm7aLWCqWivKN\nSjDaIqGx3URL6crhRC0Hnb5ba4P5PgwObKvk8CdCeHdHbWmTzJQblkRbdLpnZaz4\nv2nUW6zEj8Ey5/dXRwVkWlzfcRwxhOgZ1FOu6slqpN5DqyAGiTUNHwVtCdgEMw0o\nUhhhH/VzY5cb4eRjeUmTyrZ80JoRLH2m+/eqET/q4QKBgQDubhPlimuJda5BR0MP\n2aZBVunSZaKNEz8P8yhLOhxTAvNDP5qmH7+7L19iQsgZEmSQHp6tZfI9hkzlvMKt\nOKJDcKSFB1Gdj4y6w5CBkFx7sBxduFXodzHyP5o71HrYq7VCaV/2CRxDkZzA+aNg\nSRo+CPujdvgP2cZ7GNvzLMYX5QKBgQDka5473r/oi32tKwLJD3aKgGS43R38zxao\ne4z1M6b9xKtLDd9Sqb8jTF8mwcVg6jBTMox6ShVwAYBPFwHms7pUIKgpG9dqz0gB\nh0D2QwhDjcggV+e+HF28zSRK75+0dRQVNbQWVoDXlrA8yJpmLPFh2SuLAXnZdt9X\n9314mshbGQKBgQDT2Zz2LHqGZbjSKbZtg+8USVxy5Hl9LievTVd1GAoIvCtXilEn\n4Dfk4x+2WC4hENWntH07BsUpY4Y57vFvJk4O7CxSQwGCpQTfAVsJtDJoeD+MCnjS\nl+4aF+c71/zbPh5NBwILw2aIpv4H/QfsSqf1jNfCE7gvpUmVIK52MEdG/QKBgQDY\nEl0qMTnEFj+aEXefDfuKZI3iuXfmb1b1pXnfcS7kGqgWZVb9cQkXsOTJWr8FQELa\nUJTGEVJaE3F2X0MzIox9jC7GREnwBYgNug3fZeVpUbMftUfIdDjPohZUtHuUTrPi\npFxoTQev6CFqPjCfup/TeYVRBuJmraX0Jm8QKQqh8QKBgD+kIN8OJupy+OmFtgI4\nVYPQb4Jua6pCYJZOS6G4TloXdbchMejn67O0VB/k3s3JBG3neoD72n/RiX/Hno3U\nQxrxUYJw6r53tMSv4oDui7hS4dnJ7PNVdH+Wi1WGP+CC2BFi2qtnfpDhxgtk/1F0\nWBnLvrTbyQ+Z5xtf6GVIxe+S\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-1uno3@e-commers-web-page.iam.gserviceaccount.com",
  "client_id": "110276546586494629783",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1uno3%40e-commers-web-page.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


import pyrebase

firebase=pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database=firebase.database()


cred = credentials.Certificate(service)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
database = firestore.client()

def HomePage(request):
    return render(request,'SellerHom.html')

def Seller_Singup(request):
    Name=request.POST.get('name')
    Mobile_number=request.POST.get('Mobile_number')
    Email=request.POST.get('Email')
    password=request.POST.get('password')
    seller_data={
        'Name':Name,'Mobile_number':Mobile_number,'Email':Email,'password':password,'Type':'Seller','product_count':0,
    }
    try:
        main_id="Sell"+Name[::2]+Mobile_number[::3]+Email[::4]
        seller_data['main_id']=main_id
        database.collection('Seller').document(Email).set(seller_data)
        authe.create_user_with_email_and_password(Email,password)
        print(f'Seller account oppen & data uplod complet of {Name}')
        return render(request,'Seller-login_page.html',{ "Sdata" :seller_data })
    except:
        print("Account cant't open")
    return render(request,'Seller-Singup.html')

from django.contrib.auth import logout

def logout(request):
    Sdata=request.session['Sdata']
    print(Sdata)
    print("changing value of sdata ")
    Sdata=None
    print(Sdata)
    request.session['Sdata'] = Sdata
    try:
        print("logout is complit ..................../////=====/////..............")
        return redirect('Seller:sellerHome')
    except:
        print("log out failed")
    print("try to log out ...............;;;;;;;;;;;;;;;;;;////////////////////////////// ")
    return redirect('Seller_login')


def sellerHome(request):
    print("you are in seler home page .////////////////////////////")
    Sdata = request.session.get('Sdata')
    # Sdata = request.session.get('Sdata', {})
    print("sdata is")
    print(Sdata)
    if Sdata == None or Sdata == {}:
        return redirect('Seller:Seller_login')
    else:
        print("..................................................")
        print("seller data retreave is sucessfull")
        print(Sdata)
        print("..................................................")
        request.session['Sdata'] = Sdata
    return render(request,"sellerHome.html",{'data':Sdata})

def sellerUplod(request ):
    print("you are in seler uplod page .////////////////////////////")
    Sdata = request.session.get('Sdata', {})
    email = Sdata['Email']
    productCount = int(Sdata["product_count"])
    print('...............................................................................')
    print(Sdata)
    sellerId=Sdata["main_id"]
    print(sellerId)
    print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
    print(email)
    print(f'your total uploded product {productCount}')
    print(productCount+1)
    customer_data = {"product_count":productCount+1}
    Sdata.update(customer_data)
    print(Sdata)
    print(',.,.,.,.,.,.,.')

    
    print(Sdata)
    Name = request.POST.get('name')
    price = request.POST.get('price')
    descreption = request.POST.get('descreption')
    
    UplodedProduct_data= {'Name':Name,'price':price,'descreption':descreption,'product_count':productCount+1}
    select_opt = request.POST.get('hidden_data')
    if(select_opt == 'Clothes' or select_opt == 'Shows'):
        # color,brand,size,faeric,desine,paterns,type,model , User ,waight
        color = request.POST.get('color')
        brand = request.POST.get('brand')
        size = request.POST.get('size')
        faeric = request.POST.get('faeric')
        desine = request.POST.get('desine')
        paterns = request.POST.get('paterns')
        type = request.POST.get('type')
        model = request.POST.get('model')
        User = request.POST.get('User')
        waight = request.POST.get('waight')
        option = select_opt
        product_data = {
            'color':color,'brand':brand,'size':size,'faeric':faeric,'desine':desine,'paterns':paterns,'type':type,'model':model,
            'User':User,'waight':waight,"option":option,'seller_id':Sdata["main_id"],
        }
        UplodedProduct_data.update(product_data)
        # print(product_data)
    elif(select_opt == 'mobile' or select_opt == 'Laptop'):
        # display size , display , battery , network , brand , ram & rom , waight,camera,procacers,warrenty,model number,color,sim slort,wifi , batery type,grafic , charging -->
        displaysize = request.POST.get('displaysize')
        display = request.POST.get('display')
        battery = request.POST.get('battery')
        network = request.POST.get('network')
        brand = request.POST.get('brand')
        ramrom = request.POST.get('ram&rom')
        waight = request.POST.get('waight')
        camera = request.POST.get('camera')
        procacers = request.POST.get('procacers')
        warrenty = request.POST.get('warrenty')
        modelnumber = request.POST.get('modelnumber')
        color = request.POST.get('color')
        simslort = request.POST.get('simslort')
        wifi = request.POST.get('wifi')
        baterytype = request.POST.get('baterytype')
        grafic = request.POST.get('grafic')
        charging = request.POST.get('charging')
        option = select_opt
        product_data = {
            'displaysize':displaysize,'display':display,'battery':battery,'network':network,'brand':brand,'camera':camera,'procacers':procacers,'warrenty':warrenty,
            'modelnumber':modelnumber,'color':color,'simslort':simslort,'wifi':wifi,'baterytype':baterytype,'grafic':grafic,'charging':charging,'option':option
        }
        UplodedProduct_data.update(product_data)
        # print(product_data)
    elif(select_opt == 'Gagets'):
        # size  , battery , wireless connection , brand , waight  ,warrenty, model number ,color, batery type , type , charging   -->
        batterypresent = request.POST.get('batterypresent')
        chargable = request.POST.get('Chargable')
        brand = request.POST.get('Brand')
        weight = request.POST.get('waight')
        model_number = request.POST.get('modelnumber')
        color = request.POST.get('color')
        wireless_connection = request.POST.get('wirelessconnection')
        battery_type = request.POST.get('baterytype'),
        option = select_opt
        product_data = {
            'batterypresent': batterypresent,
            'Chargable': chargable,
            'Brand': brand,
            'waight': weight,
            'modelnumber': model_number,
            'color': color,
            'wirelessconnection': wireless_connection,
            'baterytype': battery_type,
            'option':option
        }
        UplodedProduct_data.update(product_data)
        # print(product_data)
    elif(select_opt == 'Toys'):
        age = request.POST.get('age')
        waight = request.POST.get('Waight')
        chargable = request.POST.get('Chargable')
        size = request.POST.get('Size')
        material = request.POST.get('material')
        brand = request.POST.get('Brand')
        type_ = request.POST.get('Type')
        model = request.POST.get('Model')
        user = request.POST.get('User')
        option = select_opt
        product_data = {
            'age': age,
            'Waight': waight,
            'Chargable': chargable,
            'Size': size,
            'material': material,
            'Brand': brand,
            'Type': type_,
            'Model': model,
            'User': user,
            'option':option,
        }
        UplodedProduct_data.update(product_data)
        print(product_data)
    
    import datetime
    x=datetime.datetime.now()
    x=str(x)
    p_generated=x[5:10:1]+x[11:13:1]+x[20:27:1]
    if (select_opt == 'Clothes' or select_opt == 'Shows' or select_opt == 'Laptop' or select_opt == 'mobile' or select_opt == 'Gagets' or select_opt == 'Toys'):
        # product_id="Pd"+Name[::3]+data['main_id'][::3]+str(productCount+1)+p_generated
        product_id="Pd"+Name[::3]+str(productCount+1)+p_generated
        UplodedProduct_data.update({'product_id':product_id})
        UplodedProduct_data.update({'sellerId':sellerId})
        ok=database.collection('products').document(select_opt).collection('Products').document(product_id).set(UplodedProduct_data)
        ok=database.collection(select_opt).document(product_id).set(UplodedProduct_data)
        ok=database.collection('Products').document(product_id).set(UplodedProduct_data)
        print(ok)
        database.collection('Seller').document(Sdata["Email"]).set(Sdata)
    else :
        print("bal chal data push truy """"""""""""""""""""""""""""""""""""""")
    print("data uplod Succesfull")
    print(UplodedProduct_data)
    if Name != None:
        return render(request,'UplodSuccesfull.html',{'Name':Name,'data':Sdata,'product_id':product_id})
    else:
        print("It uploding not complit")
    return render(request,'sellerUplod.html',{'data':Sdata})


def uplodSucessFull(request,Name):
    print("you are in seler login page .////////////////////////////")
    print(" after sucessfull uplod name is "+Name)
    seller_home_url = render('Seller:sellerHome')
    return render(request,'UplodSuccesfull.html',{'seller_home_url': seller_home_url})

def Seller_login(request):
    print("it is seller login ............../using firebase auth......../..")
    Sdata = None
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(f'{email} {password}')
    try :
        user = authe.sign_in_with_email_and_password(email,password)
        Sdata=database.collection('Seller').document(email).get().to_dict()
        request.session['Sdata'] = Sdata
        # print(Sdata)
        print('data is ')
        print(Sdata)
        print("../\..\/..")
    except :
        print('seller login is not complit')
    if Sdata  : 
            print('user is ')
            print(user)
            uid=user['localId']
            print(uid)
            request.session['Sdata'] = Sdata
            return redirect('Seller:sellerHome')
    else:
        print(f"fail to sign in: {email}")
    return render(request,'Seller-login_Page.html')
