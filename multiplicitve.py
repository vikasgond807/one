import re

def multInverse(num):
    i=1
    while True:
        temp=((i*26)+1)/num
        if temp==int(temp):
            return int(temp)
        i+=1

def multEncrypt(msg,key):
    msg=msg.upper()
    msg=re.sub(r'[^A-Z]','',msg)
    cText=''
    cList=[]
    for letter in msg:
        asciVal=ord(letter)
        
        cText+=chr((((asciVal-65)*key)%26)+65)
    return cText

def multDecrypt(cText,key):
    cText=cText.upper()
    cText=re.sub(r'[^A-Z]','',cText)
    dText=''
    inverseKey=multInverse(key)
    for letter in cText:
        asciVal=ord(letter)-65
        dText+=chr((((asciVal)*inverseKey)%26)+65)
    return dText

print('Key Domain: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25')
key=int(input('Enter One The following Keys: '))
msg=input('\nEnter Message to be encrptyed: ') 
cText=multEncrypt(msg,key)
print(f'\ncipher text = {cText}')
dText=multDecrypt(cText,key)
print(f'\nDeciphered text = {dText}')