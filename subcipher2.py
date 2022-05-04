

def ceaserencrypt(msg,key):
    c_text=''
    for letter in msg:
        X=str(chr((ord(letter)+key)%128))
        c_text+=X
    return c_text
def ceaserdecrypt(msg,key):
    d_text=''
    for letter in msg:
        Y=str(chr((ord(letter)-key)%128))
        d_text+=Y
    return d_text

msg=str(input("Enter string here(alphabets only):"))
key=int(input("Enter key here:"))
encrypted_text=ceaserencrypt(msg,key)
print(f"Encrypted text is:{encrypted_text}")
decrypted_text=ceaserdecrypt(encrypted_text,key)
print(f"Decrypted text is:{decrypted_text}")