Python 3.3.5 (v3.3.5:62cf4e77f785, Mar  9 2014, 10:37:12) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
import os
import re

quant = 0
files = []
m = (os.getcwd())+"{}"
roots = [root[1:] for root, dirs, files in os.walk('.')]
for root in roots:
    if root != "":
        files.append(os.listdir(path = m.format(root)))
    elif root == "":
        files.append(os.listdir(path = "."))
for i in range (len(files)):
    expansions = {}
    for j in range(len(files[i])):
        if re.search ('[.]',files[i][j]) != None:
            exp = files[i][j].rsplit('.', maxsplit = 1) [1]
            if exp in expansions:
                expansions[exp] += 1
            else:
                expansions[exp] = 1
    for key in expansions:
        if expansions[key] > 1:
            quant += 1
print("В", quant, "папках встречается несколько файлов с одинаковым расширением")


