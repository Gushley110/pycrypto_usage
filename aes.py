import url_to_base64

from Crypto.Cipher import AES
from Crypto import Random

key = b'password12345678'
cipher = AES.new(key,AES.MODE_EAX)

text = cipher.encrypt(b'hola')

print(str(text))