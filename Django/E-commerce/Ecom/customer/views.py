{
    # firebaseConfig = {
    #   'apiKey': "AIzaSyB8YHcXlJjvb10CKHrF91M0VZB6SYxEb8o",
    #   'authDomain': "ecom-56940.firebaseapp.com",
    #   'projectId': "ecom-56940",
    #   'storageBucket': "ecom-56940.appspot.com",
    #   'messagingSenderId': "905707331861",
    #   'appId': "1:905707331861:web:f84967504bc3b06396891c",
    #   'measurementId': "G-RDLMJFQGZR",
    #   'databaseURL':" ",
    # }

    # service={
    #   "type": "service_account",
    #   "project_id": "ecom-56940",
    #   "private_key_id": "195f9af1284246423cc355ed717b99830313f4df",
    #   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCr9MJZfbB1M9VJ\n6IvRt0VQYH36pubVn824BKvYuTCRLBZV1YCpz+zSCs7afeIwFtT8OsYL8MTEjie6\n8f1PDALMsqcml7+wTH4dVHzVV1+yx65rfoUmki3jrQFbmXDjvR86G9L4uCcwP/7c\nA2ittpubjHToUwggp7C/FXfP4WcvkouLXhM9u1AndJ7sxpN1HcMMKf9VihrOksH+\n08iS55m42G0qIwmC7VT6grQMNouFLWBfbNRz+R55rtHa9p8vwFd6zmBUz86izt/e\n6MsRLkq1ZjavkwfPVPW1hLDPLdto98230ayOKO9crsXJ7nAc+biTrDfDtLMOqROM\nt0pg3rupAgMBAAECggEAAd0G5UX3ia8zcBUYmH/cn5y2W77kGGyeZZt8RAuEcb6E\nAP0rt2BmJDjzKScOf1qYcV/pYyFsYvTybvT4DA0HFWyyIW+pHHGOY1WxSmMRN24M\nYDTjR+TSSdNzMLsqArXGGi743L1/RfX+i2m49UmFtgQFRt8OrBqpNe8O+qXt9OkS\nDezViJsILI/zhvcQFHT579/Y1ldkxoeF1BZ004K4EeRt98uIxIdqQHsTmj3A/M8K\nIaz7kIJ8JVB9rPh7r46aBhwAYQHHCA4u/m5hpSNfGfvbXOUNXPba81B2vxoR7siN\nZUw6iEXvPKG8gxD5OluBT7LrBxWJJ+LhFVrmCO5pNwKBgQDwZOCD9kTxBmJw4QF5\n/crV6uKTcdJmPj78ri4RzDe4SWkZeaj522c962gCFX01ng8hoSJwBidxHq72rYV0\nL79APQ5qwFJ8dTG+hJDONupUAHNyRqhidDym9ue8R3OknzetEV0g7+U98do337qa\nqfkqD2RWaPPlCKw1x7sY6dWgCwKBgQC3HoH08rFGQPVPYNlwgIGEOwxI7E0SjjYd\nPBx30wo7QpZqhM7I6afOVVLeEDWcGtH7Jlz6XxVzfCY9SQm2rsjpLKeLV3O78DHa\nNNku6NfS+YZHtHh63bT0/lwHOvT716jhMdr241T7TMQ63J+HUGk0/X2kdH0FrqN8\nbOCljmCfmwKBgQCaLvlZajDZrlChOY+q4L6h6Z8dFpnt/eqEQmtF+weZ6WvBbSiV\n6MUVD9GL1KCULSZjWWgvFaNiiF2L1cuMs7skxoRir6u4K6qWGYyO1uYArrFdEDib\nvRXRuPb06ZcgdQZOuJ5Uq8kKq/5ca+DRpkcrVOf0DCiyM5fQfqRf3Eqp9QKBgGKx\nDYdvmX1smwl6ABazG5qhnGBdArjibmXZNNqboiMIIzsrcqszyt3YfH30LICCr/L0\n3R2PS2dfXNig2ZxcnSmWiIH/0v9SV/vribXPhipNk0JoEJrfjJyRzhWTf9+PfpRI\nI2P2Z6G84PF8YHo0K0+E40dUBOGgGrp/j5+KmabLAoGBALj9EKAPk0Funa3hn8Wi\n5bON6O3nuCOObd37IswWPajzG9YqYaB6JNjOHTrAG98blv8LO7DetwgZjxV4HeNL\n16iv/jfH8l02C/xp5eh8PE/tD0TGwzYsh8nlS76pT86+r5G3bHAEREyrRSbD6RuB\nd437vK6/UufIxGlF5iuthoUG\n-----END PRIVATE KEY-----\n",
    #   "client_email": "firebase-adminsdk-mr0hg@ecom-56940.iam.gserviceaccount.com",
    #   "client_id": "112109638455070073064",
    #   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #   "token_uri": "https://oauth2.googleapis.com/token",
    #   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-mr0hg%40ecom-56940.iam.gserviceaccount.com",
    #   "universe_domain": "googleapis.com"
    # }
}


from django.shortcuts import render,redirect
import pyrebase
import firebase_admin
from firebase_admin import credentials , firestore

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
    email = request.POST.get('email')
    password = request.POST.get('password')
    # email='1st@g.com'
    # password='123456'
    print(f'{email} {password}')
    data=database.collection('customer').document(email).get().to_dict()
    
    if data  : 
        if(data["Email"] == email and data["password"]==password ):
            print(data["Email"])
            # core=auth.sign_in_with_email_and_password(email,password)
            print('sayan basani command have to be fllow \n \n \n ok ok ok ')
            print(data)
            print("sucess to sign up")
            return render(request,"HomePage.html",{"data":data})
            # return redirect(f"/doctor/doc-dashboard?doc_id={email}")
            # return render(request, "appointments_req.html", {"pat_ids": pat_id, "data": appointment_requests})
    else:
        # print(f"fail to sign in")
        print(f"fail to sign in: {email}")
    return render(request,"login_page.html")


############## singup 
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
        # return redirect('homepage:HomePage')
        return redirect('customer:user_login')
    except:
        print("Account cant't open")
    return render(request,'Singup.html')