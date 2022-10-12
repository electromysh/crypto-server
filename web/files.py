extension = '.encoded'
outcoming_path = '/home/user/outcoming_data/'

def save(path, data):
    name = path.split('/')[-1:][0]
    new_path = outcoming_path + name
    file = open(new_path, 'wb')
    file.write(data)
    file.close()
    
    return new_path
    
def read(path):
    file = open(path, 'r+b')
    data = file.read()
    file.close()
    
    return data

def apply_extension(path):
    last_index = path.rfind(extension)
    
    if last_index != -1:
        return path
    
    new_path = path + extension
    
    return new_path
    
def remove_extension(path):
    last_index = path.rfind(extension)
    
    if last_index == -1:
        return path
    
    ends_at = last_index + len(extension)
    new_path = path[:last_index] + path[ends_at:]
    
    return new_path
