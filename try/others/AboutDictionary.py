'''print a specific element of dictionary'''
# x={'s1':12,'s2':"sayan",'s3':True}
# print(x['s1'])
# print(x['s2'])
# print(x['s3'])
'''use loop in dictionery'''
# for i,a  in x.items ():
#     print(f'{i}:{a}')
    
'''make a dictionery'''
# x1={}
# n=int(input("enter number :- "))
# for i  in range(0,n):
#     a=input("Enter name :- ")
#     b=int(input("Enter get num :- "))
#     x1[a]={b}
# print(x1)    


'''   print the histry value from the discenary  '''
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# value=sampleDict['class']['student']['marks']['history']
# print(value)

''' if any key have to be delete '''
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

# for k in keys:
#     sample_dict.pop(k) 
# print(sample_dict)

s = {
    "name": "sayan basani ",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a=s['name']
print(a[1:3])