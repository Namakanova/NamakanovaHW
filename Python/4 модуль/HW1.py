import re


def opening(fname):
    sentences = []
    words = []
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    new_text = re.sub('[\.\?\!…]', 'q', text)
    sentences = new_text.split('q')
    for a in range(len(sentences)):
        sentences[a] = re.sub('[\.,*<>«»:;\'\"\n–-]','', sentences[a])
        sentences[a] = sentences[a].strip()
    return (sentences)


def creating_list(sentences):
    true_sentences = [[sentence, (len(sentence) - (len(sentence.split(' ')) - 1)) / (len(sentence.split(' ')))] for sentence in sentences if len(sentence.split(' ')) > 10 ]
    template = "Предложение \"{}\" со словами длины {:.1f}"
    for a in true_sentences:
        print(template.format(a[0], a[1]))
    

def main():
    sentences = opening(input("Введите имя файла: "))
    creating_list(sentences)


main()
