import requests, sys, os, re

if len(sys.argv)<3:
    print('use .py file, the URL <URL> and the path <path>')
    exit()

# please try this site for test purposes : sys.argv[1]='https://statsroyale.com/cards'
r = requests.get(sys.argv[1])
pattern=re.compile(r'(https://)[a-zA-Z0-9-_./]+(jpg|png|gif)')

listOfImages=[]
matches = pattern.finditer(r.text)
for match in matches:
        listOfImages.append(match[0])

for img in listOfImages:
    with open(os.path.join(sys.argv[2],img.split("/")[-1]), 'wb') as f:
        f.write(requests.get(img).content)
