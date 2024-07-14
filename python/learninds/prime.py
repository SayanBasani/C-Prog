x=int(input("enter any no."))
s=0
for i in range (2,x):
    if (x%i==0):
        s=1
if(s==1):
    print(" not prime number")   
else:         
    print(" prime number")        
        