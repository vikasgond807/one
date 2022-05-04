import math
def stringifyList(arr):
    stng=""
    for i in arr:
        stng+=str(i)
    return stng

def ceaserEncrypt(msg,key):
    cText=''
    for letter in msg:
        X=str(chr((ord(letter)+key)%128))
        cText+=X
    return cText
def ceaserDecrypt(msg,key):
    dText=''
    for letter in msg:
        X=str(chr((ord(letter)-key)%128))
        dText+=X
    return dText
def altTransEncrypt(msg):
    t1=[]
    t2=[]
    flag=True
    for val in msg:
        if flag:
            t1.append(val)
            flag=False
        else:
            t2.append(val)
            flag=True
    return stringifyList(t1)+stringifyList(t2)
def altTransDecrypt(msg):
    dtext=''
    halflen= math.ceil(len(msg)/2)
    halfmsg1=msg[0:halflen]
    halfmsg2=msg[halflen:len(msg)]
    vari=0
    for letter in halfmsg2:
        dtext+=halfmsg1[vari]+letter
        vari+=1
    if len(halfmsg1)>len(halfmsg2):
        dtext+=halfmsg1[vari]
    return dtext
print("\n\nEnter Your String[Alphabets and Spaces only]")
msg=input()
print("\nEnter Your Key[Number only]")
key=int(input())
ceaserEncrypted=ceaserEncrypt(msg,key)
print (f'\n\nCeaserEncryptedText: {ceaserEncrypted}')

transEncrypted=altTransEncrypt(ceaserEncrypted)
print (f'\n\nTransEncryptedText: {transEncrypted}')

transDecrypted=altTransDecrypt(transEncrypted)
print (f'\n\nTransDecryptedText: {transDecrypted}')
ceaserDecrypted=ceaserDecrypt(transDecrypted,key)
print (f'\n\nCeaserDecryptedText: {ceaserDecrypted}')
