#voter eligablity check
age =int (input("enter age :-"))

if(age>18):
    print("you are eligable for vote")
else:
    if(age<=-1):
        print("invalid input")
    else:
        print(f"you are not eligable for vote \n you have to wait for {18-age} years")