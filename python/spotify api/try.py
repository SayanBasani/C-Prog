


inst = "1. Happiness                2. Sadness                3. Fear                   \n4. Anger                    5. Disgust                6. Depression             \n7. Joy                      8. Love                   9. Enjoyment              \n10. Sympathy                11. Surprise              12. Irritability \n                 13. Empty mood      14. multiple mood\n         15. Search according need"
print(inst)
choise = input("E nter according our choise :- ")
clen = len(choise)

            

for i in range(len(inst)):
    # if clen == 1 and inst[i-1] != "1":
    if clen == 1 :
        if inst[i] == choise[clen - 1] and inst[i + 1] == "." and inst[i - 1] != "1":
            userChose = inst[i+3:i + 21]
            userChose=userChose.strip()
            # print(userChose)
            break
    else:
        if choise[clen - 2] == inst[i] and choise[clen - 1] == inst[i + 1]:
            userChose = inst[i+3:i + 25]
            userChose=userChose.strip()
            # withOutSpace(userChose)
            break
            
print(userChose)
print(len(userChose))
if(int(choise)<14):
    print("ok generat the finale serch")
elif(int(choise)==13):
    print("")