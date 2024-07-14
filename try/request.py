# import requests as rq
# import json

# x=rq.get('http://worldtimeapi.org/api/timezone/asia/kolkata').text
# y=json.loads(x)
# print(y'datetime'[0:10])
# import json
# x={
#     "name":"sayan",
#     "age":9735154080,
#     'sex':'male'
# }
# print(x['name'])
# print(type(x))
# # y=json.dumps(x)
# # print(type(y))
# # print(y)

import json as j,requests as r
print("x")
for i in range(0,1,-2):
    x=r.get('http://worldtimeapi.org/api/timezone/asia/kolkata').text
    y=j.loads(x)
    print(y['datetime'][11:19])






