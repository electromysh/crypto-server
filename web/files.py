import os

encoded_extension = '.encoded'

def write_file(path, data):
    file = open(path, 'r+b')
    file.write(data)
    file.close()
    
def read_file(path):
    file = open(path, 'r+b')
    data = file.read()
    file.close()
    
    return data

def add_encoded_extension(path):
    last_extension_index = path.rfind(encoded_extension)
    
    if last_extension_index != -1:
        return path
    
    new_path = path + encoded_extension
    os.rename(path, new_path)
    
    return new_path
    
def remove_encoded_extension(path):
    last_extension_index = path.rfind(encoded_extension)
    
    if last_extension_index == -1:
        return path
    
    extension_ends_at = last_extension_index + len(encoded_extension)
    new_path = path[:last_extension_index] + path[extension_ends_at:]
    
    os.rename(path, new_path)
    
    return new_path
