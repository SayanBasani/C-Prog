from django.shortcuts import render,redirect,HttpResponse,HttpResponsePermanentRedirect,HttpResponseRedirect
from firebase_admin import credentials , storage , firestore
import firebase_admin , firebase ,pyrebase,json
from django.urls import reverse
import time

firebaseConfig = {
    "apiKey": "AIzaSyAvOY6_emeY0ZsdhA1s8x2NG0wNF7riYgw",
    "authDomain": "e-commers-web-page2.firebaseapp.com",
    "projectId": "e-commers-web-page2",
    "storageBucket": "e-commers-web-page2.appspot.com",
    "messagingSenderId": "852097607313",
    "appId": "1:852097607313:web:20cb7cf9bebe7e493c8130",
    "measurementId": "G-9FHK9WTB15",
    'databaseURL':" ",
}
service={
  "type": "service_account",
  "project_id": "e-commers-web-page2",
  "private_key_id": "5fef07ff64a8f4dcb3080ad4f22c34b9b4a23e49",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC9GeLgY7QQN/RI\n2uE5KiRsUgbksig0uxNr0mEZR/Sus9oiafu7mSM4PGbvpSYrZDeGQPnud3/ofd1b\nRfA4kw7ys9pFTQWCTQb+GNTieAVXc5dYnVpl9jS97P62xKsvG6f/Cs08+FHn+zNx\nZmy7SSDxXu/3fN9DtBf4qtTQ4QgqM3AELW4zWzDeuMnqChgzSkbc89H3u2Z/ibTl\ncz2Y2cmjqi6/5rGdRx31jK0os5hiXCZ6r+j5uVGADVLMII6FpO1QfdrnY1nELTTO\nNkGI0U768Z/raHtw6hgFOat1RzQRhj5c1D/AiFK4UOsZoBNZ1lwgxXjXZceZw9WE\nWxZyAg7fAgMBAAECggEACgB1gd15fPtzU0B9yx08gfIwuns7KdbUkc5geQrXmT9F\nWVlLtEIcR8bXbEjK5QlO79iTSkFN0Ek1TQo883EWcvsqSfdnRDC4yaBx72yJCSAX\nBYaFF9bW4U4eBs1jfywHowi6OZr/Z2AKT4QrBMOQbNPS/hRqZqqpiJXYiG0ZQR9n\nMAeiEyYjWkrFuSymitypGnVpHntNGGKz407NrX/llidtzxiRNMP7y72EcO5MWJpN\nlG3/coWhYeArEdqQkjPF5O/iDo4KkSNc5N83MP/Fa5D+YlhUKQAtEm5LMtIuwqvQ\neoXz39ceN4Bks8e+SXyKCJOWXtfWa9trHmTaXZqHEQKBgQD9UrRMdSik60FE3gW5\nDWPsjuLWr7o3bmiBT5Q0WqEcphOM12M3vKuQfP1cXPF8eV0GfviPi2p3h6DrNTUG\n8IdPxrSJpVmQ4/D9mv1ZHYqQQelVsO0IBOLKKrMNud/2Qqcm0RqO91wRkhjelU8K\nwD6E+Ti+WLaubHxK2i8muMzNOQKBgQC/GXJ6L57NmXSD5NKXQ2bJP5PnxHDhl+b1\n1+TruoXxyx7xlO7iuXOOed21shOZEvicxAmU6xCmQqeQrMhxS8dSsnJeMv1RsCl0\nW5yngsOyyGmbil0JBjvh3CXx6pE+4KCsxz5su6iFS3H1nAotwXyZdDArbxXoPBYp\nBRyXuwNU1wKBgQD5B1arWvlLtuGA++oQUvOKV6Tze+jKGUWu6TY+iWGcsj7B0/N7\nlYPrFJRVOiFDRmOGwUdEhb9yJeixkKrCWa4LZMGSFvSHlS0Rgk3QT1QqIEFrtfQu\nT+9K4tMGiVV712ZOqH09Ujo2I7NDDPCZFwfe3MlFhhyAN7GwO/DiVgUvMQKBgGwW\nLJXHkX6gqTJgnmxIBz8U4sdYaLBwhoXO0wAxw8j7Jkll/6flVOLlMu2uBz+xZ0Tj\n7Ld6LTScxsIhuE28msS/gcid9oHZrdjOaFCmuaHJkVIUdILCL+ST7DJkhjqWOsr+\n9uPxUGP0RESzOV6f7aWt/gDTGAT+11nkNkPr1vqJAoGBAOtcbFKAQC324uD0cPS+\n+ytr4LKpBb87WScwBZAXfNkqmx53dmA2WLCnKPxAdZEXQthYmMlbrx6DnKlDwBEV\nLCUJ75gL19oDh49MoDNQQW5rF8GsVvjwVjsVR55YdL6OVntg5cMg9d/WJjU6ypvy\n0FAmm0Cxwco98B7IiYy3XWkN\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-9cgxk@e-commers-web-page2.iam.gserviceaccount.com",
  "client_id": "114862640897417925426",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9cgxk%40e-commers-web-page2.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
if not firebase_admin._apps:
    print("firebase_admin.initialize_app(cred) have to ineasealize ")
    cred = credentials.Certificate(service)
    firebase_admin.initialize_app(cred)
database = firestore.client()
# print(auth)


# Create your views here.
def HomePage(request):
    c_data = None
    print('c_data is : ')
    c_data = request.session.get('c_data')
    print(c_data)
    request.session['c_data']=c_data
    return render(request,'HomePage.html',{'c_data':c_data})
def produc(request):
    c_data = None
    c_data = request.session.get('c_data')
    # print(c_data)
    type = request.GET.get('type')
    id = request.GET.get('id')
    print(f'| product type is {type} | product is : {id} | ')
    p_data = database.collection(type).document(id).get().to_dict()
    print(f'data is {p_data}')
    return render(request , 'product.html',{'l_p_data':p_data})

def product(request):
    c_data = None
    c_data = request.session.get('c_data')
    # print(f'customer data is {c_data}')
    try :
        if request.session.get('id'):
            id = request.session.get('id')
        if request.GET.get('id'):
            id = request.GET.get('id')
        print(f'| product is : {id} | ')
        p_data = database.collection('Products').document(id).get().to_dict()
        # print(f'product data is {p_data}')
        return render(request , 'product.html',{'l_p_data':p_data,'id':id , 'c_data':c_data})
    except:
        id = None
        print(f'product data is ot found | id is {id}')
        return HomePage(request)
def addToCart(request):
    print("................................. working started .................................")
    id = request.GET.get('id')
    try:
        request.session['id']=id
        print("session create is sucess")
    except:
        print("session create is faill")
    print(f'product id is {id}')
    c_data = None
    # cartCount = 0
    c_data = request.session.get('c_data')
    import datetime
    carrentDate = str(datetime.datetime.now())
    print(carrentDate)
    if c_data != None :
        c_cart_data = database.collection('cart').document(c_data['Email']).get().to_dict()
        if c_cart_data != None:
            cartCount = len(c_cart_data)
            print(f'cart data is :{c_cart_data}\ncart value is {cartCount}')
        addCart = None
        if c_cart_data != None:
            print("working in part 1 ................./////////////////////.....................")
            # print(f'cart count is {c_cart_data['cartCount']}')
            print("sayan")
            addCart = {
                str(cartCount+1):{
                    'cartCount':cartCount+1,
                    'productId':id,
                    'Time':carrentDate,
                }
            }
            print(f'have to send this --->\n{addCart}')

            c_cart_data.update(addCart)
            print(f'have to send this data into database {c_cart_data != None}')
            i=0
            i_check = True
            while(i<cartCount):
                # print(f'count is{c_cart_data[str(i+1)]['productId']}')
                if c_cart_data[str(i+1)]['productId'] == addCart[str(cartCount+1)]['productId'] :
                    print("they are same")
                    i_check = False
                    break
                i+=1
            if (i_check):
                database.collection('cart').document(c_data['Email']).set(c_cart_data)
                print('uplod complit')
                c_data=database.collection('customer').document(c_data['Email']).get().to_dict()
                print(f' user data is : {c_data}')
                c_data.update({'cartCount':cartCount})
                database.collection('customer').document(c_data['Email']).set(c_data)
                print(f'newly user data is seted data is : {c_data}')
            else:
                print("it already into the cart")
            # data i add in user basic ditels (only the cart total product)
            # c_data=database.collection('customer').document(c_data['Email']).set(c_data)

            c_cart_data.update(addCart)
        else:
            print("working in part 2 ................./////////////////////.....................")
            cartCount = "1"
            addCart ={
                cartCount : {
                'cartCount':cartCount,
                'productId':id,
                'Time':carrentDate,
                }
            }
            print(f'have to send this --->\n{addCart}')
            # previous approtch
            # database.collection('cart').document(c_data['Email']).collection(cartCount).document('productData').set(addCart)
            # try new 
            database.collection('cart').document(c_data['Email']).set(addCart)
        print("cart function is working")
    if (c_data == None):
        print('you have to login ..................................??')
        return redirect(reverse('customer:user_login'))
    return redirect(reverse('homepage:product'))

 