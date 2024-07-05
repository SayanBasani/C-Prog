from django.shortcuts import render,redirect
import firebase_admin
import firebase_admin,pyrebase
from firebase_admin import credentials , firestore
from firebase_admin import credentials, initialize_app, storage

firebaseConfig = {
    "apiKey": "AIzaSyAvOY6_emeY0ZsdhA1s8x2NG0wNF7riYgw",
    "authDomain": "e-commers-web-page2.firebaseapp.com",
    "projectId": "e-commers-web-page2",
    "storageBucket": "e-commers-web-page2.appspot.com",
    "messagingSenderId": "852097607313",
    "appId": "1:852097607313:web:20cb7cf9bebe7e493c8130",
    "measurementId": "G-9FHK9WTB15",
    'databaseURL':"https://e-commers-web-page2-default-rtdb.firebaseio.com/",
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
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
  "universe_domain": "googleapis.com",
  
}

cred=credentials.Certificate(service)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
database = firestore.client()
storage = firebase.storage()

# ####### singup

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
        return render(request,"login_page.html",{"c_data":customer_data})
    except:
        print("Account cant't open")
    return render(request,'Singup.html')

############ login
def user_login(request):
    c_data = None
    c_data = request.session.get('c_data')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(f'{email} {password}')
    c_data=database.collection('customer').document(email).get().to_dict()
    request.session['c_data'] = c_data
    if c_data  : 
        if(c_data["Email"] == email and c_data["password"]==password and c_data["Type"]=="Customer"):
            print(c_data["Email"])
            # core=auth.sign_in_with_email_and_password(email,password)
            print('sayan basani command have to be fllow \n \n \n ok ok ok ')
            page_T={
                'page_T':"Customer"
            }
            c_data.update(page_T)
            print(c_data)
            print("sucess to sign up")
            return redirect("homepage:HomePage")
    else:
        print(f"fail to sign in: {email}")
    return render(request,"login_page.html")
def logOutCustomer(request):
    print("try to log out")
    return redirect('customer:user_login')

def cart(request):
    c_data = request.session.get('c_data')
    # print(f'customer data is {c_data}')
    c_Email = c_data['Email']
    # print(f'customer mail is {c_Email}')
    userCartData = database.collection('cart').document(c_Email).get().to_dict()
    # print(f'cart data of {c_Email} is \n{userCartData}')
    cartDataLen = len(userCartData)
    print(f'cart data lenth is {cartDataLen}')
    allCardItems = {}
    for i in range (0,cartDataLen):
        p_id = userCartData[str(i+1)]['productId']
        print(f'{i}th product id is : {p_id}')
        CartProductData = database.collection('Products').document(p_id).get().to_dict()
        # print(f'item {i} --> {CartProductData} \n')
        allCardItems.update({f'{i}':CartProductData})
        print(allCardItems)
        print('\n')
    return render(request , "cart.html",{'cartItems':allCardItems})
def order(request):
    return render(request , "order.html")
def product_list(request):
    c_data=request.session.get('c_data')
    # print(c_data)
    print('you are in produce list -------------------------------------------------------------')
    search = request.GET.get('search')
    print(f'User search {search}')
    docs = database.collection("Products").stream()
    # print(docs)
    product = []
    for doc in docs:
        p_data = doc.to_dict()
        for key, value in p_data.items():
            # print(f'{key} --> {value}')
            # print(f'{value} ===== {search}\n')
            if isinstance(value, str) and value.lower() == search.lower():
            # if value == "5":
                # print(f"{doc.id} => {doc.to_dict()} \n")
                product.append(p_data)
    print(type(product))
    # print(product)
    print('.....................................................')
    # print(p_data)
    print(p_data['Name'])
    return render(request , "product_list.html",{'c_data':c_data,'products':product})

def uplod(path):
    storage.child("Images").child('img.png').put(path)
    url = storage.child("Images").child('img.png').get_url(firebaseConfig['storageBucket'])
    r_url = str(url)
    return r_url    
items = {
    "0": {
    "option": "Laptop",
    "network": "5g",
    "price": "46",
    "ProductImg": "https://firebasestorage.googleapis.com/v0/b/e-commers-web-page2.appspot.com/o/Laptop%2FLaptopPd4207-0307407522?alt=media&token=e-commers-web-page2.appspot.com",
    "Name": "456",
    "product_id": "Pd4207-0307407522",
    "product_count": 2,
    "sellerId": "SellSle111s@o"
  },
  "1": {
    "option": "Laptop",
    "network": "5g",
    "price": "46",
    "ProductImg": "https://firebasestorage.googleapis.com/v0/b/e-commers-web-page2.appspot.com/o/Laptop%2FLaptopPda107-0215446409?alt=media&token=e-commers-web-page2.appspot.com",
    "Name": "a1",
    "product_id": "Pda107-0215446409",
    "product_count": 1,
    "sellerId": "Sells45s."
  },
  "2": {
    "option": "Laptop",
    "network": "5g",
    "price": "56456",
    "ProductImg": "https://firebasestorage.googleapis.com/v0/b/e-commers-web-page2.appspot.com/o/Laptop%2FLaptopPdl107-0307155932?alt=media&token=e-commers-web-page2.appspot.com",
    "Name": "lap",
    "product_id": "Pdl107-0307155932",
    "product_count": 1,
    "sellerId": "Sells45s."
  },
}
# for i in items:
#     print(i.Name)