x=int(input("enter any no"))
a=1
for i in range (2,x):
    if x%i==0:
        print(i)
        a=a*i
        j=x