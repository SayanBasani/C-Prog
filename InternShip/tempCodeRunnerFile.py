num={}
nn=int(input("enter your end number : "))
for i in range(1,nn,2):
    # print(i)
    num[(i**2)]=((i+1)**2)
b=num.items()

for k,l in num.items():
    print (f'{k} --->> {l}')
# print('00000')