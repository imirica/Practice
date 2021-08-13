#pornind de la un url, descarca toate imaginile de pe pagina respectiva || foloseste sys.argv pentru a introduce URLul
"""open the source page , find in it all images extension; download it"""

# re libs
# raw String : put r in front of the string ex : print(r'\tTAB') vs print('\tTAB')

# import re
# import sys
#
# if len(sys.argv)<2:
#     print('please add a text to search')
#     exit()
#
# tts = """
# abcfsfs
# ABCasdas
#
# 123412123
# @#)!@((#!
#
# """
# #
# # pattern = re.compile(sys.argv[1])
# # matches=pattern.finditer(tts)
# #
# # for match in matches:
# #     print(match)
"""import requests
import sys
import os

l=['https://cdn.statsroyale.com/images/cards/full/electrogiant.png','https://cdn.statsroyale.com/images/cards/full/royal_recruits.png']

for i in l:
    r=requests.get(i)
    filename=i.split("/")[-1]
    save_path= sys.argv[1]
    complete_name = os.path.join(save_path,filename)
    with open(complete_name, 'wb') as f:
        f.write(r.content)"""
import requests
import re, os





# f = open('test1', 'w')
# f.write(r.text)
# f.close()

# pattern=re.compile(r'(https://)[a-zA-Z./]+(png)]')

# for line in open('test1'):
#     for match in re.finditer(pattern,line):
#         l.append(line)
# print(l)
#
# f.close()



r = requests.get('https://statsroyale.com/cards')
pattern=re.compile(r'(https://)[a-zA-Z0-9-_./]+(jpg|png|gif)')

l=[]
with open('test1', 'r') as f2:
    content=f2.read()

    matches = pattern.finditer(content)

    for match in matches:
        l.append(match[0])
print(l)

# /([a-z\-_0-9\/\:\.]*\.(jpg|jpeg|png|gif))/i
# (http)?s?:?(\/\/[^"']*\.(?:png|jpg|jpeg|gif|png|svg))
#
# str1="""
# https://cdn.statsroyale.com/images/cards/full/electro_dragon.png
# https://cdn.statsroyale.com/images/guide-2b.jpg
# https://cdn.statsroyale.com/images/guide-3b.gif
# https://cdn.statsroyale.com/images/cards/full/goblin_giant.png
# https://cdn.statsroyale.com/images/cards/full/minion_horde.png"""
#
# pattern=re.compile(r'(https://)[a-zA-Z0-9-_./]+(jpg|png|gif)')
# matches=pattern.finditer(str1)
#
# for i in matches:
#     print(i[0])


