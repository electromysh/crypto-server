from flask import Blueprint, request
from enum import Enum
from .files import read_file, write_file, add_encoded_extension, remove_encoded_extension
from .algorythms.AES_CBC import encrypt_AES_CBC, decrypt_AES_CBC
from .algorythms.AES_ECB import decrypt_AES_ECB, encrypt_AES_ECB
from .algorythms.BLOWFISH_CBC import decrypt_blowfish_CBC, encrypt_blowfish_CBC


views = Blueprint('views', __name__)

AES_CBC = 'AES_CBC'
AES_ECB = 'AES_ECB'
BLOWFISH_CBC = 'BLOWFISH_CBC'
CEASAR = 'CEASAR'

algorythmTOCode = {
    AES_CBC: b'of98aens',
    AES_ECB: b'0r8gn082',
    BLOWFISH_CBC: b'24457e7w',
    CEASAR: b'2e2dsplq'
}

codeToAlgorythm = {
    algorythmTOCode[AES_CBC]: AES_CBC,
    algorythmTOCode[AES_ECB]: AES_ECB,
    algorythmTOCode[BLOWFISH_CBC]: BLOWFISH_CBC,
    algorythmTOCode[CEASAR]: CEASAR
}

divider = b"uhfofhcldzskvp;ajvd23928392edpjos"

@views.route('/encrypt', methods=['POST'])
def encrypt():
    path = request.get_json(True)['path']
    password = request.get_json(True)['password']
    algorythm = request.get_json(True)['crypto_algo']
    
    file_data = read_file(path)
    
    data_to_edcode = file_data + divider + bytes(password, 'utf-8')
    
    if algorythm == AES_CBC:
        write_file(
            path,
            encrypt_AES_CBC(data_to_edcode) + algorythmTOCode[AES_CBC]
        )
        new_path = add_encoded_extension(path)
        
        return '{"path": "' + new_path + '"}'
    elif algorythm == AES_ECB:
        write_file(
            path,
            encrypt_AES_ECB(data_to_edcode) + algorythmTOCode[AES_ECB]
        )
        new_path = add_encoded_extension(path)
        
        return '{"path": "' + new_path + '"}'
    elif algorythm == BLOWFISH_CBC:
        write_file(
            path,
            encrypt_blowfish_CBC(data_to_edcode) + algorythmTOCode[BLOWFISH_CBC]
        )
        new_path = add_encoded_extension(path)
        
        return '{"path": "' + new_path + '"}'
    else:
        return '{"error": "Wrong param \"crypto_algo\": ' + algorythm + '"}'

@views.route('/decrypt', methods=['POST'])
def decrypt():
    path = request.get_json(True)['path']
    password = request.get_json(True)['password']
    file_data = read_file(path)
    
    algorythm_code = file_data[-8:]
    data_to_decrypt = file_data[:-8]
    
    if codeToAlgorythm[algorythm_code] == AES_CBC:
        decoded_data = decrypt_AES_CBC(data_to_decrypt)
    elif codeToAlgorythm[algorythm_code] == AES_ECB:
        decoded_data = decrypt_AES_ECB(data_to_decrypt)
    elif codeToAlgorythm[algorythm_code] == BLOWFISH_CBC:
        decoded_data = decrypt_blowfish_CBC(data_to_decrypt)
    else:
        return '{"error": "Can not decode"}'
        
    splitted_data = decoded_data.split(divider)
    
    if len(splitted_data) != 2:
        return '{"error": "Can not decode"}'
    
    if splitted_data[1] == bytes(password, 'utf-8'):
        write_file(path, splitted_data[0])
        new_path = remove_encoded_extension(path)
        
        return '{"path": "' + new_path + '"}'
    else:
        return '{"error": "Incorrect password"}'

