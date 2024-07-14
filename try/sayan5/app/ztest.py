from firebase import Firebase
config = {
    "apiKey": "AIzaSyB8ZcdT24jdW3WXzbOmtEEf1ek_0jJY4hY",
    "authDomain": "sayan-f3d45.firebaseapp.com",
    "projectId": "sayan-f3d45",
    "storageBucket": "sayan-f3d45.appspot.com",
    "messagingSenderId": "606881739618",
    "appId": "1:606881739618:web:5dd89a97338df824d4723b",
    "measurementId": "G-FW1TXGNPWG",
    "databaseURL" : "https://sayan-f3d45-default-rtdb.asia-southeast1.firebasedatabase.app/",
}
firebase = Firebase(config)
db =firebase.database()
# data = {
#     "name": "Sayan Basani",
#     "mobile":9735154080,
#     "age":20
# }
# db.set(data)
# db.update({
#     "eduction":{
#         "trad":"diploma in computer sciance and technology",
#         "year":"2nd year",
#         "sem":"3rd sem"
#     }
# })


data=db.get()
print(data)
for item in data.each():
    print(item.val()) #this is extrect or print data of the items
    print(item.key())# this is print key of items
























# db.set(data)
# #using "set" we uplod data on the firebase data base add remove all old data
# db.push(data)
#using "push" we upload data on firebase in a signeficent or specific key ,key is auto genreted
# db.child("personal ditels").set(data) 
# using "child" we use "set" and "push" to uplod data on a specifice created directery
# db.update({"CV":"no achivement "})
# using "update" we add new data in data base with out remove other data