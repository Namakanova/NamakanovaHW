import re

def read(name):
    f = open(name, 'r', encoding = 'utf-8')
    words = f.read().replace('\n', ' ').split()
    f.close()
    return words

def delete(words):
    for i, word in enumerate(words) :
        words[i] = word.lower().strip('.,/1234567890@#$%^&*><~`|\}{][!?():;-_=+"\'')
    return words

def print(words):
    for word in words:
        if re.search('загру(з(ят(ся)?|и(шь(ся)?|(сь)?|м(ся)?|л((ся)?|а(сь)?|и(сь)?|о(сь)?)|т((ся)?|е(сь)?|ь(ся)?)|в(ш(ую(ся)?|ая(ся)?|е(го(ся)?|му?(ся)?|й(ся)?|е(ся)?|ю(ся)?)|и((сь)?|й(ся)?|м(и)?(ся)?|е(ся)?|х(ся)?)))?))|ж(у(сь)?|ен(а|о|ы)?|ён|(е|ё)нн(ая|ую|о(м(у)?|ю|е|го|й)|ы(м(и)?|й|е|х))))$', word):       
            print(word)

def main():
    words = deleting(reading(input('Введите имя файла:\n')))
    printing(words)



main()
