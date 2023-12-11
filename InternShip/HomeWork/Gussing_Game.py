import random
x = a = int(random.random()*100)
# print(x)
y = 0
for i in range(0, a):
    y = a = y + 1
    print(f" Try No. {y}")
    n = int(input("Enter any number :- "))
    if (n == x):
        print("it is correct")
        break
    elif (n < x+10 and n > x-10):
        print("You are too close")
    elif (n > x):
        print("you are too high")
    elif (n < x):
        print("you are too low")
print(f"Total atampt is {y}")
