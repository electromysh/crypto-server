def write_file(path, data):
    file = open(path, 'r+b')
    file.write(data)
    file.close()
    
def read_file(path):
    file = open(path, 'r+b')
    data = file.read()
    file.close()
    
    return data