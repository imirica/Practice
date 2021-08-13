import requests, sys, os, re

if len(sys.argv)<3:
    print('use .py file, the url <url> and the path <path>')
    exit()

# please try this site for test purposes : sys.argv[1]='https://statsroyale.com/cards'
r = requests.get(sys.argv[1])
pattern=re.compile(r'(https://)[a-zA-Z0-9-_./]+(jpg|png|gif)')

# other regex to get image URL from HTML(found on internet) - it does't work
# /([a-z\-_0-9\/\:\.]*\.(jpg|jpeg|png|gif))/i
# (http)?s?:?(\/\/[^"']*\.(?:png|jpg|jpeg|gif|png|svg))

#am pus codul sursa al paginii intr-un .txt, ca ulterior sa il parcurg si sa pun match-urile intr-o lista
f = open('test1', 'w')
f.write(r.text)
f.close()

listOfImages=[]
with open('test1', 'r') as f2:
    content=f2.read()

    matches = pattern.finditer(content)

    for match in matches:
        listOfImages.append(match[0])

for img in listOfImages:
    r=requests.get(img)
    filename=img.split("/")[-1]
    save_path= sys.argv[2]
    complete_name = os.path.join(save_path,filename)
    with open(complete_name, 'wb') as f:
        f.write(r.content)