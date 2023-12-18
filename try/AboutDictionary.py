'''print a specific element of dictionary'''
# x={'s1':12,'s2':"sayan",'s3':True}
# print(x['s1'])
# print(x['s2'])
# print(x['s3'])
'''use loop in dictionery'''
# for i,a  in x.items ():
#     print(f'{i}:{a}')
    
    
x1={}
n=int(input("enter number :- "))
for i  in range(0,n):
    a=input("Enter name :- ")
    b=int(input("Enter get num :- "))
    x1[a]={b}
print(x1)    

# # for i,j in x.items():
# #     print(i,"=",j)


# print(x.items())




# shop={'1st':'chocklet','2nd':'books','3rd':100,'quality':'good','4th':{
#     'owner':'sayan','age':19,'sex':'male'
# }}
# print(shop['2nd'])
# # x=shop.items()
# # print(x)
# for i,a in shop.items():
#     print(f"{i}:{a}")
# # shop.append('sayan')
# print(shop)


# '''   print the histry value from the discenary  '''
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
