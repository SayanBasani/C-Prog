from django.shortcuts import render,redirect
from django.urls import reverse
import firebase,pyrebase,firebase_admin
from firebase_admin import credentials , firestore,storage
import json

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
  "universe_domain": "googleapis.com"
}


cred = credentials.Certificate(service)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
database = firestore.client()
storage = firebase.storage()
def HomePage(request):
    return render(request,'SellerHom.html')

def Seller_Singup(request):
    Name=request.POST.get('name')
    Mobile_number=request.POST.get('Mobile_number')
    Email=request.POST.get('Email')
    password=request.POST.get('password')
    s_data={
        'Name':Name,'Mobile_number':Mobile_number,'Email':Email,'password':password,'Type':'Seller','product_count':0,
    }
    try:
        main_id="Sell"+Name[::2]+Mobile_number[::3]+Email[::4]
        s_data['main_id']=main_id
        database.collection('Seller').document(Email).set(s_data)
        print(f'Seller account oppen & data uplod complet of {Name}')
        return render(request,'Seller-login_page.html',{ "data" :s_data })
    except:
        print("Account cant't open")
    return render(request,'Seller-Singup.html')


def Seller_login(request):
    s_data = None
    request.session['s_data'] = s_data
    print("you are in seler login page .////////////////////////////")
    email = request.POST.get('email')
    password = request.POST.get('password')
    # password='123456'
    print(f'{email} {password}')
    s_data=database.collection('Seller').document(email).get().to_dict()
    print(s_data)
    
    if s_data  : 
        if(s_data["Email"] == email and s_data["password"]==password and s_data["Type"]=="Seller"):
            page_T={
                'page_T':"Seller"
            }
            s_data.update(page_T)
            print(s_data)
            print("Seller sucess to sign up")
            request.session['s_data'] = s_data
            return redirect('Seller:sellerHome')
    else:
        print(f"fail to sign in: {email}")
    return render(request,'Seller-login_Page.html')

from django.contrib.auth import logout

def logout(request):
    return redirect('Seller_login')


def sellerHome(request):
    print("you are in seler home page .////////////////////////////")
    s_data = request.session.get('s_data', {})
    
    if s_data == None or s_data == {}:
        return redirect('Seller:Seller_login')
    else:
        print("..................................................")
        print(s_data)
        print("..................................................")
        request.session['s_data'] = s_data
    return render(request,"sellerHome.html",{'s_data':s_data})

def sellerUplod(request ):
    print("you are in seler uplod page .////////////////////////////")
    s_data = request.session.get('s_data', {})
    email = s_data['Email']
    
    productCount = int(s_data["product_count"])
    print('...............................................................................')
    print(s_data)
    sellerId=s_data["main_id"]
    # print(f'{sellerId}  {email}')
    # print(f'your total uploded product {productCount}')
    # print(productCount+1)
    customer_data = {"product_count":productCount+1}
    s_data.update(customer_data)
    # print(s_data)
    # print(',.,.,.,.,.,.,.')

    
    # print(s_data)
    Name = request.POST.get('name')
    price = request.POST.get('price')
    descreption = request.POST.get('descreption')
    select_opt = request.POST.get('hidden_data')
    
    # generate unique name for product 
    import datetime
    x=datetime.datetime.now()
    x=str(x)
    p_generated=x[5:10:1]+x[11:13:1]+x[20:27:1]
    product_id=""
    if Name:
        product_id="Pd"+Name[::3]+str(productCount+1)+p_generated
    print(f'name is {Name}')
    # product_id is the name 
    path = request.POST.get('image')
    if path:
        path  = path.replace("\\","\\\\",1000)
        path = path.replace('"','',1000)
        print(f'the modefied path after replace is : {path}')
    print(f'the modefied path is : {path}')
    # this line is help to uplod image
    if path:
        if storage.child(str(select_opt)).child(f'{select_opt}{product_id}').put(path) :
            # storage.child(str(select_opt)).child(f'{select_opt}{product_id}').put(path)
            print("uplode is succes full ...........///////////..............")
        else :
            return render(request,'sellerUplod.html',{'s_data':s_data})
    url = storage.child(str(select_opt)).child(f'{select_opt}{product_id}').get_url(firebaseConfig['storageBucket'])
    r_url = str(url)   
     
    print(f'uploded image link is : {r_url}')
    UplodedProduct_data= {'Name':Name,'price':price,'descreption':descreption,'product_count':productCount+1,'ProductImg':r_url}
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
            'User':User,'waight':waight,"option":option,'seller_id':s_data["main_id"],
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
    
    
    if (select_opt == 'Clothes' or select_opt == 'Shows' or select_opt == 'Laptop' or select_opt == 'mobile' or select_opt == 'Gagets' or select_opt == 'Toys'):
        # product_id="Pd"+Name[::3]+data['main_id'][::3]+str(productCount+1)+p_generated
        
        UplodedProduct_data.update({'product_id':product_id})
        UplodedProduct_data.update({'sellerId':sellerId})
        ok=database.collection('products').document(select_opt).collection('Products').document(product_id).set(UplodedProduct_data)
        ok=database.collection(select_opt).document(product_id).set(UplodedProduct_data)
        ok=database.collection('Products').document(product_id).set(UplodedProduct_data)
        print(ok)
        database.collection('Seller').document(s_data["Email"]).set(s_data)
    else :
        print("bal chal data push truy """"""""""""""""""""""""""""""""""""""")
    print("data uplod Succesfull")
    print(UplodedProduct_data)
    if Name != None:
        return render(request,'UplodSuccesfull.html',{'Name':Name,'s_data':s_data,'product_id':product_id})
    else:
        print("It uploding not complit")
    return render(request,'sellerUplod.html',{'s_data':s_data})


def uplodSucessFull(request,Name):
    print("you are in seler login page .////////////////////////////")
    print(" after sucessfull uplod name is "+Name)
    seller_home_url = render('Seller:sellerHome')
    return render(request,'UplodSuccesfull.html',{'seller_home_url': seller_home_url})


# from firebase import storage

def upload_image_to_firebase(image_file):
    # Initialize Firebase Admin SDK
    # Make sure you have set up Firebase Admin SDK and initialized it properly
    
    # Upload image to Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob("images/" + image_file.name)
    blob.upload_from_string(image_file.read(), content_type=image_file.content_type)
    # Get public URL of the uploaded image
    return blob.public_url
    # path = "C:\\Users\\sayan\\Pictures\\Screenshots\\Screenshot 2024-04-27 200632.png"
    # path = "C:\Users\sayan\Pictures\Wallpaper\surgery-1807541.jpg"
    # upload_image_to_firebase(path)
    # storage.child("ok").child(f'sayan').put(path)
