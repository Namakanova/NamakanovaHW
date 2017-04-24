import re
import os

am = 0
data = []
z = (os.getcwd())+"{}"
roots = [root[1:] for root, dirs, files in os.walk('.')]
for root in roots:
    if root != "":
        data.append(os.listdir(path = t.format(root)))
    elif root == "":
        data.append(os.listdir(path = "."))
for i in range (len(data)):
    extensions = {}
    for j in range(len(data[i])):
        if re.search ('[.]',data[i][j]) != None:
            ext = data[i][j].rsplit('.', maxsplit = 1) [1]
            if ext in extensions:
                extensions[ext] += 1
            else:
                extensions[ext] = 1
    for key in extensions:
        if extensions[key] > 1:
            am += 1
print("В", am, "папках находится несколько файлов одного расширения")
