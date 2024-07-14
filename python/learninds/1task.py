'''
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
expected answer :- {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', "salary": 8000}
'''

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# x=len(employees)
# sayan={}
# for i in range (0,x):
#     sayan[employees[i]]=defaults
# print(sayan)

'''
sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"}
# Keys to extract
keys = ["name", "salary"]

expected answer :-{'name': 'Kelly', 'salary': 8000}
'''
# sample_dict = {
# "name": "Kelly",
# "age": 25,
# "salary": 8000,
# "city": "New york"}
# # Keys to extract
# keys = ["name", "salary"]
# a=0
# keys_len=(len(keys)+1)
# boys={}
# for i in range(0,(keys_len-1)):
#     for k,l in sample_dict.items():
#         if (keys[i]==k):
#             boys[keys[i]]=l
#         else:
#             keys_len=keys_len+1
# print(boys)



# for i,j in reversed(sample_dict):
#     for k in range(0,n):
#         if(i==keys[k]):
#             continue
#         else:
#             print(f'{i}:{j}')

# print(new.reversed())


'''
sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:
200 present in a dict
'''
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# x=0
# for i,j in sample_dict.items():
#     if(j==200):
#         x=1
# if(x==1):
#     print("200 present in a dict ")
# else:print("200 not present in a dict")

'''
sample_dict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}
Expected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
'''
# sample_dict = {
# "name": "Kelly",
# "age":25,
# "salary": 8000,
# "city": "New york"
# }
# sample_dict["city"]=["location"]
# print(sample_dict)


'''
sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"
}
keys = ["name", "salary"]
Expected output:
{'city': 'New york', 'age': 25}
'''

# solution :-1

# sample_dict = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}
# keys = ["name", "salary"]
# UpKeys=[]
# RevDict={ii:sample_dict[ii] for ii in reversed(sample_dict)}
# m=0
# for i,j in sample_dict.items():
#     if(i!=keys[m]):
#         UpKeys.append(i)
#         m=m+1
# m=0
# UpKeys.reverse()
# # print(UpKeys)
# sample={}
# for d,e in RevDict.items():
#     if(UpKeys[m]==d):
#         sample[d]=e
#         if(m<len(keys)-1):
#             m=m+1
#         else:
#             break
# print(sample)

# solution :- 2
# sample_dict = {
# "name": "Kelly",
# "age": 25,
# "salary": 8000,
# "city": "New york"
# }
# # Keys to remove
# keys = ["name", "salary"]
# a=0
# for i,j in sample_dict.items():
#     if(i==keys[a]):
#         continue
#     else:
#         print(f'{i}:{j}')
    # a+=1
    
# solution :- 3
# for k in keys:
#     sample_dict.pop(k) 
# print(sample_dict)

# sample_dict = {
# "name": "Kelly",
# "age": 25,
# "salary": 8000,
# "city": "New york"
# }
# # Output:- 
# # {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}


# import requests
# x=requests.get("https://www.google.com")
# print(x.text)

'''
sample_dict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}
Expected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
'''

# sample_dict = {
# "name": "Kelly",
# "age":25,
# "salary": 8000,
# "city": "New york"
# }
# item=input("which iteme you want to remove :- ")
# it=sample_dict[item]
# sample_dict.pop(item)
# item_name=input("enter new name :- ")
# sample_dict.update({item_name:it})
# print(sample_dict)



'''
# Get the key of a minimum value from the following dictionary
sample_dict = {
'Physics': 82,
'Math': 65,
'history': 75
}
Expected output:
Math
'''
sample_dict = {
'Physics': 82,
'Math': 65,
'history': 75
}

'''Answer 1'''
# def low(a,b):
#     if(a>b):
#         return b
#     else:
#         return a
# e1=1000
# k=''
# for i,j in sample_dict.items():
#     e1=low(j,e1)
#     if(e1==j):
#         k=i
# print(k)
'''answer 2'''
# x=1000
# for i,j in sample_dict.items():
#     x=min(x,j)
# print(x)


'''
Change value of a key in a nested dictionary
change Brad's salary to 8500 in the following dictionary.
Given:
sample_dict = {
'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 500}
}
Expected output:
{
'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 8500}
}
 '''
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500}, 
#     'emp2': {'name': 'Emma', 'salary': 8000}, 
#     'emp3': {'name': 'Brad', 'salary': 500}
#     }
# sample_dict['emp3']['salary']=sample_dict['emp3']['salary']+sample_dict['emp2']['salary']
# print(sample_dict['emp3']['salary'])
# # print(x)

'''
###Convert two lists into a dictionary###
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# New_Dict={}
# for i in range(0,len(keys)-1):
#     New_Dict[keys[i]]= values[i]
# print(New_Dict)
    
    
    
'''
Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# for i,j in dict2.items():
#     dict1[i]=j
# print(dict1)