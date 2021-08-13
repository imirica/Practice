#parcurge tot systemul si afiseaza fisierele care apar exact de doua ori

#parcurg cu os.walk()
#generez pentru fiecare fisiere un o valoare sha 256
#valoarea sha256 va deveni cheia unui dictionar ce va stoca valoarea fisierului respectiv
""" USE OS
import os

os.chdir('/Users/iulim/OneDrive/Desktop/test')
print(os.listdir())
for dirpath, dirnames, filenames in os.walk('/Users/iulim/OneDrive/Desktop/test/'):
    print('dirpath :', dirpath)
    print('dirnames :', dirnames)
    print('filenames : ', filenames)"""

"""USE DICTS
newDict={}
newDict["a"]="a"
print(newDict)"""

"""# Append multiple value to a key in dictionary
def add_values_in_dict(sample_dict, key, list_of_values):
    #Append multiple values to a key in the given dictionary
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict"""

import hashlib

#https://docs.python.org/3/library/hashlib.html

#b " " - Feeding string objects into update() is not supported, as hashes work on bytes, not on characters.
#use sha256() to create a SHA-256 hash object
#SHA 256 - cryptographic hash function
#DIGEST - A small change in the input (in the word "over") drastically changes the output (digest)
#hash.digest() - Return the digest of the data passed to the update() method so far. This is a bytes object of size digest_size which may contain bytes in the whole range from 0 to 255.
#hash.hexdigest() Like digest() except the digest is returned as a string object of double length, containing only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments.
#hash.update(data) - Update the hash object with the bytes-like object. Repeated calls are equivalent to a single call with the concatenation of all the arguments: m.update(a); m.update(b) is equivalent to m.update(a+b).
#hash.digest_size - The size of the resulting hash in bytes.
#hash.block_size - The internal block size of the hash algorithm in bytes.

"""
str = hashlib.sha256(b'1')

str_hex = str.hexdigest()
strh_hex = str.digest()

print(hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest())
"""


"""
sha256 needs to be calculated based on file contents. You will need to basically read file contents and pipe it though sha256. 
hashlib.sha256(open('filename.exe','rb').read()).hexdigest()

# Open,close, read file and calculate MD5 on its contents 
# using 'with' the file will be closed as we exit from that block of code
with open(file_name) as file_to_check:
    # read contents of the file
    data = file_to_check.read()    
    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()
"""

"""f = open('test.txt', 'r')
print(f.mode)
f.close()"""

"""Python can work with the following file formats:

Comma-separated values (CSV)
XLSX
ZIP
Plain Text (txt)
JSON
XML
HTML
Images
Hierarchical Data Format
PDF
DOCX
MP3
MP4
SQL
"""

