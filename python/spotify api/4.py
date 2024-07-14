import requests as rq 
import json
from time import sleep
for i in range(0,1000,1):
    x=rq.get('http://worldtimeapi.org/api/timezone/asia/kolkata').text
    y=json.loads(x)
    print(f" Time :-- {y['datetime'][11:19]} ") 
