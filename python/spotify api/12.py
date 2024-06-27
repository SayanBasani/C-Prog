# it is complitly working (Spotify auth and serch )
import requests,base64,json,webbrowser
from flask import Flask, request, render_template, redirect, url_for

client_id = 'ad2c9eac11164c1daedfb242259eac63'
client_secret = '09449177104a4e2d8229d930f5780613'

combined = f"{client_id}:{client_secret}"
encoded_bytes = base64.b64encode(combined.encode('utf-8'))
encoded_str = encoded_bytes.decode('utf-8')
# print(combined,"\n",encoded_bytes,"\n",encoded_str)

headers = {
    'Authorization':f'Basic {encoded_str}',
    "Content-Type": "application/x-www-form-urlencoded",
}
data = {
    "grant_type": "client_credentials"
}
aut_url = 'https://accounts.spotify.com/api/token'
x = requests.post(aut_url,headers = headers,data = data)
y=x.text
y=json.loads(y)
access_token = y['access_token']
access_token = f'Bearer {access_token}'

###### search in spotify
url = "https://api.spotify.com/v1/search" 
search = input("enter song name or mood :- ")
params = {
    'q':search,
    'type':'track',
}
headers = {
    'Authorization':access_token,
}

a = requests.get(url,params=params,headers=headers)
data = a.text
data = json.loads(data)
# print(data)
# print("\n\n\n\n")
# print(data)
# print("\n\n\n\n")
# Extract the URI of the first track
track_uri = data['tracks']['items'][0]['uri']
print(f'Track URI: {track_uri}')
preview_url = data['tracks']['items'][0]['preview_url']
# webbrowser.open()
redirect("F:\study disk(E)\Programing\C-Prog\python\spotify api\12.html",preview_url=preview_url)











# key = data['tracks']["items"]['album']['artists']
# key = data["tracks"]["items"]
# print(key)



# url = "https://api.spotify.com/v1/tracks/{id}" #search in spotify
# search = input("enter song name or mood :- ")
# params = {
#     'q':search,
#     'type':'track',
# }
# headers = {
#     'Authorization':access_token,
# }

# a = requests.get(url,params=params,headers=headers)
# print(a.text)

