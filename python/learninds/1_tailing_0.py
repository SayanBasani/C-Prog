# x=int(input("Enter any  number :- "))
x=101
def factorial(number):
    for i in range(1,number):
        number=number*(number-1)
        return number
a=str(factorial(x))
b=0
y=len(a)
print(f'{a} type :- {type(a)} length :- {len(a)} y:- {y}')
for i in range(0,y,1):
    if(a[i]=='1'):
        for j in range(i,(y)):
            if (a[j]=='0'):
                b=b+1
        break
    break
print(b)
        