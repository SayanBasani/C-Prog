import requests as r
import json

x=r.get('http://worldtimeapi.org/api/timezone/asia/kolkata').text
y=json.loads(x)
print(x)
# print(f" Time :-- {y['datetime'][11:19]} ") 
# print(f" Time :-- {y['datetime'][11:19]} ") 
print(f"Date :- {y['datetime'][0:10]} Time :-- {y['datetime'][11:19]} ") 





# x=r.get('http://worldtimeapi.org/api/timezone/asia/kolkata')
# # print(x)
# y=json.load(x)
# print(y)
