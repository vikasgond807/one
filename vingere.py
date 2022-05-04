import re

def vignereEncrypt(msg,key):
    index=0;
    cText=''
    for letter in msg:
        num=ord(letter)-65
        newno=(num+(ord(key[index%len(key)])-65))%26
        cText+=chr(newno+65)
        index+=1
    print (cText)
    return cText
def vignereDecrypt(cText,key):
    index=0;
    dText=''
    for letter in cText:
        num=ord(letter)-65
        newno=(num-(ord(key[index%len(key)])-65))%26
        dText+=chr(newno+65)
        index+=1
    print (dText)
    return dText

msg="hello world"
key="jash"
msg=re.sub(r'[^A-Z]','',msg.upper())
key=re.sub(r'[^A-Z]','',key.upper())
print(msg)
print(key)
cText=vignereEncrypt(msg,key)
vignereDecrypt(cText,key)
