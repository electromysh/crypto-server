import binascii
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


#inputs
plaintext = 'fhodfdsvnhsdnvlsdl'
key = pad(b"my_key", AES.block_size)
iv = pad(b"my_iv", AES.block_size)

# Encryption
def encrypt_AES_ECB(plaintext):
    data_bytes = plaintext
    padded_bytes = pad(data_bytes, AES.block_size)
    AES_obj = AES.new(key, AES.MODE_ECB)
    cyphertext = AES_obj.encrypt(padded_bytes)
    return cyphertext

# ciphertext = encrypt_AES_ECB(plaintext)
# print(ciphertext)
# print(binascii.hexlify(ciphertext))

# Decryption
def decrypt_AES_ECB(ciphertext):
    AES_obj = AES.new(key, AES.MODE_ECB)
    raw_bytes = AES_obj.decrypt(ciphertext)
    extracted_bytes = unpad(raw_bytes, AES.block_size)
    return extracted_bytes

# plaintext = decrypt_AES_ECB(ciphertext)
# print(plaintext)
# print(plaintext.decode('ascii'))