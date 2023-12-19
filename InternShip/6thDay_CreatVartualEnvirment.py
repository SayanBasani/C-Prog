'''
#### How to creat a vartual envirment on PC ###
step 1 :- open terminal |
          "mkdir Folder_Name" Use to creat a new folder |
          "cd folder_name" to open a folder |
          'dir' use to see all file or folder present in the present Path
step 1 :- open this folder where you want to creat the vartual envirment
step 2 :- then open this file on the terminal  
step 3 :- then run "py -m venv Name_Vartual_Envirment
step 4 :- then "cd Name_Vartual_Envirment"
step 5 :- run " Script\activates"
'''


import requests as rq 
import json
from time import sleep
for i in range(0,1000,1):
    x=rq.get('http://worldtimeapi.org/api/timezone/asia/kolkata').text
    y=json.loads(x)
    # print(f" Time :-- {y['datetime'][11:19]} ") 
    # print(f" Time :-- {y['datetime'][11:19]} ") 
    print(f"Date :- {y['datetime'][0:10]} Time :-- {y['datetime'][11:19]} ") 
    sleep(2)
