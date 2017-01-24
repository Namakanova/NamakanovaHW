def words():
    d = {}
    with open ("words.csv", 'r', encoding='utf-8') as f:
        for word in f.readlines():
            word = word.replace('\n', '').split(",")
            d[word[0]] = word[1]
    return d


def playing(d):
    q = len(d)
    for key, val in d.items():
        i = 3
        print("Это должно помочь: ", key, "...")
        print("У Вас ", i, "попыток(и)")
        print("Поехали!")
        s = str(input())
        i = 2
        while s != val:
            print("Неверно!")
            if i == 0:
                print("Опять не то : (")
                print("Было загадано слово:", val)
                print("Словосочетание целиком:", key, val)
                print("----------------------------")
                print("Хотите ещё раз?")
                a = str(input())
                if a == "нет" or a == "Нет":
                    print("Приходите снова!")
                    return a
                elif a == "да" or a == "Да":
                    q -= 1
                    break
            if s != val:
                print("Помощь: ", key, "...")
                print("Осталось", i, "попыток(и)")
                s = str(input())
                i -= 1
        if s == val:
            print("Правильно!")
            q -= 1
            print("Здесь есть еще ", q, "загадок(и)")
            if q == 0:
                print("На сегодня всё!")
                break
            else:
                print("Еще?")                
                d = str(input())
                if d == "нет" or d == "Нет":
                    print("Приходите снова!")
                    break

def welcoming():
    print("Привет! Я хочу сыграть с тобой в игру")
    print("Давай проверим твой словарный запас,а?")
    a = str(input())
    if a == "нет" or a == "Нет":
        print("Ну ладно, как захочешь, приходи!")
    elif a == "да" or a == "Да" or a == "Давай" or a == "давай":
        print("Приступим")
        print("__________________________")
        playing(words())
            
welcoming()
