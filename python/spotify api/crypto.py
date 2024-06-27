wal = "ed25519:5GS6JpnVQVYKwhz339Re2trZYBdAq7BGARC7cer4JcRmAXYW8eBUSzVqiWKzwZdPqmum2nDNDCmHmkYB5RtWLVDS"
wall = "5GS6JpnVQVYKwhz339Re2trZYBdAq7BGARC7cer4JcRmAXYW8eBUSzVqiWKzwZdPqmum2nDNDCmHmkYB5RtWLVDS"
# print(len(wall)) #97 - 122 , 65 - 90 , 48 - 57
# for i in range (0,200):
#     print(f'{i} : {chr(i)}')

wordarr =[]
for i in range (0,200):
    if 47<i<58 or 64 < i<= 90 or 96 < i < 123:
        wordarr.append(chr(i))
print(f'len of arr id {len(wordarr)}')
# for i in range (0 , len(wordarr)):
#     print(wordarr[i])

# print(total)

for i in range (0 , len(wordarr)):
    print(f'')


# for i in range (0,90):
def arangeStr(i):
    while(i<30):
        














total = 1
for i in range (0,88):
    total = total*62