# sum even and odd between 100 using function make it dinamic

def form(range1):
    even=[]
    odd=[]
    for i in range(0,range1):
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    sum=[]
    for j in range (0,int(range1/2)):
        sum.append(even[j]+odd[j])
    return sum
x=int(input("Enter any number :- "))
print(form(x))