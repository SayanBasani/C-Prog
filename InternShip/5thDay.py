# dictionary
# syntex
'''
{
    key:value # key should be unique
}
'''
# x={
#     'name':'sayan basani',
#     'mob':9735154080
# }
# print(x)
''' 
# data insersen methord

DictioneryName[key]=value
'''
# x['email']='sayanbasani1@gmail.com'
# print(x)
'''
# how to find all the key from the dictionery

dictioneryname.keys
'''
# a=x.keys()
'''
dictioneryname.values
'''
# a=x.values()
'''
dictioneryname.items
'''
# a=x.items()
# print(a)


# for print all data on by one and stractured
# for i,j in x.items() :
#     print(f'{i} --> {j}')


# x['mobile']='poco x4 pro'
# for i,j in x.items() :
#     print(i,j)

    
    
''' task   ///take 5 data from use and print'''

# x={}
# a=int(input("Enter number of product :- "))
# for i in range(0,a):
#     name=input("enter name of item :- ")
#     prod=input("enter data :- ")
#     x[name]=prod
# for y,j in x.items() :
#     print(f'{y}-->{j}')


''' task ///'''
# x={}
# z=0
# # a=int(input("Enter number of product :- "))
# for i in range(0,10):
#     x[i]=i**2
# for j,k in x.items():
#     print(f'{j}= {k}')
#     z=z+k
# print(z)

'''
you have to print :-
1  4
9  16
25  36.... 
'''
num={}
for i in range(0,100,2):
    # print(i)
    num[(i**2)]=((i+1)**2)
b=num.items()

for k,l in num.items():
    print (f'{k}     {l}')
#     print(num)