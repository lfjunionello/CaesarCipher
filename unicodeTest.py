letter = 'A'
uni = ord(letter)
""" uni+=25 """
print(uni)

#UPPERCASE
if (uni < 65):
    uni+=26
elif (uni > 90):
    uni-=26

#LOWERCASE
if (uni < 97):
    uni+=26
elif (uni > 122):
    uni-=26

print(chr(uni))

""" word = 'Arquivo não encontrado!'
for i in word:
    print(i) """