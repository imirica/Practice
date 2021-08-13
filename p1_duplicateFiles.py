import datetime
import os
import hashlib
import timeit
import sys

start = datetime.datetime.now()

def addValuesInDict(sampleDict, key, listOfValues): # regula celor 3 : nu faci functie decat daca folosesti bucata de cod de mai mult de 3 ori
    if key not in sampleDict:
        sampleDict[key] = []
    sampleDict[key].append(listOfValues)

# path='C:/Users/iulim/OneDrive/Desktop/test/' - hardcodat
newDict={}
print(sys.argv)
#daca numarul de parametrii introdusi in terminal este mai mic de 2, printeaza mesajul
if len(sys.argv)<2:
    print('use duplicateFile.py and the path <path>')
    exit()

#_ - wildcard; sys.argv - o lista de parametrii introdusi in terminal; sys.argv[1] - primul element din lista
for dirpath, _, filenames in os.walk(sys.argv[1]):
    for element in filenames:
        #'rb' - read as byte(cate 8 biti)
        with open(os.path.join(dirpath,element), 'rb') as f: #join method used to create the absolute path of the file
            sha256=hashlib.sha256(f.read()).hexdigest()
            addValuesInDict(newDict,sha256,element)
duplicateFiles=0
for k,v in newDict.items():
    if len(v)>2:
        duplicateFiles+=1;
print('The number of files with exactly two matches is : ' + str(duplicateFiles))

stop=datetime.datetime.now()
print(stop-start)
print("text")