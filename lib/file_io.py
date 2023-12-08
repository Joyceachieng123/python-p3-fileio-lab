def write_file(file_name, file_content):
    pass
    file_name = str(file_name) + ".txt"  
    with open(file_name, "w") as file:
        file.write(file_content)
  

def append_file(file_name, append_content):
    file_name = str(file_name) + ".txt"  
    if not append_content.endswith('\n'):
        append_content += '\n'  
    with open(file_name, "a") as file:
        file.write(append_content)
pass 


def read_file(file_name):
    pass
    file_name = str(file_name) + ".txt"  
    with open(file_name, "r") as file:
        content = file.read()
    return content