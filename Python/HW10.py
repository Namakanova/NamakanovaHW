import re


def main():
    with open('Финляндия.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('Финл(я|я́)нд([а-я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','Малайз\\2', text)
    new_text2 = re.sub('ФИНЛЯНД([А-Я]{,3}([\s\&,.!\?:;<"\(\)\'» —-]))','МАЛАЙЗ\\1', new_text)
    with open('Малайзия.html', 'w', encoding = 'utf-8') as f:
        f.write(new_text2)   
    print("Файл \"Малайзия\"был создан.")


main()
