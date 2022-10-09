from Crypto.Cipher import Blowfish
from Crypto import Random
import base64

key = b'\x1b\xcf\xa2\x1d\xc3h\x8f\x19\xbf\x7f\x89\xc0\xbbe\x1eO'

def encrypt_blowfish_CBC(msg):
    iv = Random.new().read(Blowfish.block_size)
    padding = b"*"
    p = lambda s: s + ((Blowfish.block_size) - len(s) % Blowfish.block_size) * padding
    c = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    encrypted_message = iv + c.encrypt(p(msg))
    return encrypted_message

def decrypt_blowfish_CBC(encrypted_message):
    blocksize = Blowfish.block_size
    encrypted_message_ = encrypted_message[8:]
    iv = encrypted_message[:blocksize]
    d = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return d.decrypt(encrypted_message_).rstrip(b'*')

# def encrypt_blowfish_CBC(msg):
#     iv = Random.new().read(Blowfish.block_size)
#     padding = "*"
#     p = lambda s: s + ((Blowfish.block_size) - len(s) % Blowfish.block_size) * padding
#     c = Blowfish.new(key, Blowfish.MODE_CBC, iv)
#     encrypted_message = iv + c.encrypt(p(msg).encode('ascii'))
#     return base64.b64encode(encrypted_message)

# def decrypt_blowfish_CBC(encrypted_message):
#     blocksize = Blowfish.block_size
#     encrypted_message_ = base64.b64decode(encrypted_message)[8:]
#     iv = base64.b64decode(encrypted_message)[:blocksize]
#     d = Blowfish.new(key, Blowfish.MODE_CBC, iv)
#     return d.decrypt(encrypted_message_).decode().rstrip('*')
