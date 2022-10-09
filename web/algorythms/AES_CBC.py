import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

plaintext = "AAA32674A.jpg"
# print(plaintext)
key = pad(b"my_key", AES.block_size)
iv = pad(b"my_iv", AES.block_size)


def encrypt_AES_CBC(plaintext):
    data_bytes = plaintext
    padded_bytes = pad(data_bytes, AES.block_size)
    AES_obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = AES_obj.encrypt(padded_bytes)
    return ciphertext
# ciphertext = encrypt_AES_CBC(plaintext)
# print(ciphertext)
# print(binascii.hexlify(ciphertext))

def decrypt_AES_CBC(ciphertext):
    AES_obj = AES.new(key, AES.MODE_CBC, iv)
    raw_bytes = AES_obj.decrypt(ciphertext)
    extracted_bytes = unpad(raw_bytes, AES.block_size)
    return extracted_bytes

# plaintext = decrypt_AES_CBC(ciphertext)
# print(plaintext)
# print(plaintext.decode('ascii'))
    
    



