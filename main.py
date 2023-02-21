
# Online Python - IDE, Editor, Compiler, Interpreter

import sys
import hashlib

def process(filename):
    h = hashlib.sha1()
    
    with open(filename, 'rb') as file:
        shunk = 0
        while chunk !=b'': 
            chunk = file.read(1)
            h.update(chunk)

    return h.hexdigest()
            
print(process(sys.argv[1]))
