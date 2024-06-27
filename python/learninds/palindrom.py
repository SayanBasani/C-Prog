# word=input("enter name :- ")
# # word='sayan'
# x=len(word)
# # print(x)
# s=''
# for i in range (x-1,-1,-1):
#     # print(word[i])
#     d=0
#     s=s+word[i]
#     d+1
    
# if(s==word):
#     print("yes,this is palindrom.")
# else:
#     print("no,this is not a palindrom")




word=input("enter name :- ")
x=len(word)
s=''
for i in range (x-1,-1,-1):
    d=0
    s=s+word[i]
    d+1
    
if(s==word):
    print("yes,this is palindrom.")
else:
    print("no,this is not a palindrom")a