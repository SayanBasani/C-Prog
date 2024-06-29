from django.shortcuts import render,redirect
import pyrebase
import firebase_admin
from firebase_admin import credentials , firestore
from google.cloud.firestore_v1.base_query import FieldFilter

firebaseConfig = {
  'apiKey': "AIzaSyA1l6YTxtr8Xx7KcdPytaKs2YsGblMMNJk",
  'authDomain': "e-commers-web-page.firebaseapp.com",
  'projectId': "e-commers-web-page",
  'storageBucket': "e-commers-web-page.appspot.com",
  'messagingSenderId': "620595830414",
  'appId': "1:620595830414:web:9456fb464b28906f7d73df",
  'measurementId': "G-XQFMT37DGZ",
  'databaseURL':" ",
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

cred=credentials.Certificate(service)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
database = firestore.client()
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()

############ login
def user_login(request):
    data = None
    data = request.session.get('data')
    email = request.POST.get('email')
    password = request.POST.get('password')
    # email='1st@g.com'
    # password='123456'
    print(f'{email} {password}')
    data=database.collection('customer').document(email).get().to_dict()
    request.session['data'] = data
    if data  : 
        if(data["Email"] == email and data["password"]==password ):
            print(data["Email"])
            # core=auth.sign_in_with_email_and_password(email,password)
            print('sayan basani command have to be fllow \n \n \n ok ok ok ')
            print(data)
            print("sucess to sign up")
            return redirect("homepage:HomePage")
    else:
        print(f"fail to sign in: {email}")
    return render(request,"login_page.html")
def logOutCustomer(request):
    data = request.session['data']
    print(data)
    print('after empty')
    data = None
    print(data)
    request.session['data'] = data
    print("try to log out")
    return redirect('customer:user_login')
def Singup(request):
    Name=request.POST.get('name')
    Mobile_number=request.POST.get('Mobile_number')
    Email=request.POST.get('Email')
    password=request.POST.get('password')
    customer_data={
        'Name':Name,'Mobile_number':Mobile_number,'Email':Email,'password':password,'Type':'Customer' ,
    }
    # print(customer_data)
    try:
        main_id=Name[::2]+Mobile_number[::3]+Email[::4]
        customer_data['main_id']=main_id
        database.collection('customer').document(Email).set(customer_data)
        print(f'account oppen & data uplod complet of {Name}')
        return redirect('customer:user_login')
    except:
        print("Account cant't open")
    return render(request,'Singup.html')
def cart(request):
    return render(request , "cart.html")
def order(request):
    return render(request , "order.html")
def product_list(request):
    datas=request.session.get('data')
    print(datas)
    print('you are in produce list -------------------------------------------------------------')
    search = request.GET.get('search')
    print(f'User search {search}')
    docs = database.collection("Products").stream()
    print(docs)
    product = []
    for doc in docs:
        data = doc.to_dict()
        for key, value in data.items():
            if value == search:
            # if value == "5":
                print(f"{doc.id} => {doc.to_dict()} \n")
                product.append(data)
    print(type(product))
    print(product)
    print('.....................................................')
    print(data)
    print(data['Name'])
    return render(request , "product_list.html",{'data':datas,'products':product})
