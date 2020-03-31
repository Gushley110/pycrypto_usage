import url_to_base64 as b64
from Crypto.Cipher import AES
from Crypto import Random

key = 'password12345678'
test_string = 'https://open.spotify.com/collection/tracks'

def AESencrypt(key,text):
    if(len(key) != 16):
        print('Error')

    cipher = AES.new(key.encode(),AES.MODE_EAX)
    nonce = cipher.nonce
    text = b64.url_to_base64(text)
    
    return (cipher.encrypt(text),nonce)

def AESdecrypt(key,text,nonce):
    key = key.encode()
    cipher = AES.new(key,AES.MODE_EAX,nonce)
    return b64.base64_to_str(cipher.decrypt(text))

cipher_text,nonce = AESencrypt(key,test_string)
decipher_text = AESdecrypt(key,cipher_text,nonce)

print(cipher_text)
print(decipher_text)