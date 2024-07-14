import requests as rq


on = 'https://blynk.cloud/external/api/update?token=lgd5lX_v-vaB8hKXHLQcjHHZiSxnXDOY&v1=1'
off = 'https://blynk.cloud/external/api/update?token=lgd5lX_v-vaB8hKXHLQcjHHZiSxnXDOY&v1=0'

data = input('Enter choice: ')

if data == 'on':
    rq.get(on)
elif data == 'off':
    rq.get(off)
        

