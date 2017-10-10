import urllib.request
import re
import os
import time


def inUrl(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return html

# Количество страниц
def numPage():
    rePage = re.compile('<span class="b-paginator__current">\d+</span>', re.DOTALL)
    page = re.sub('<.*?>', '', rePage.search(inUrl(
        'http://orda-gazeta.ru/article/?page=10000')).group())
    return page

# Поиск ссылок на все статьи
def artOnPage(nPage):
    arrHref = []
    reArt = re.compile('<h2 class="b-object__list__item__title">.*?</h2>', re.DOTALL)
    reHref = re.compile('/\d+', re.DOTALL)
    artHref = reArt.findall(inUrl('http://orda-gazeta.ru/article/?page=%s' % str(nPage)))
    for hr in artHref:
       arrHref.append('http://orda-gazeta.ru/article' + reHref.search(hr).group()+'/')
    return arrHref

def infoArt():
    reTitle = re.compile('<h1 class="b-object__detail__title">.*?</h1>', re.DOTALL)
    reAutor = re.compile('<span class="b-object__detail__author__name">.*?</span>', re.DOTALL)
    reDate = re.compile('<span class="date">.*?</span>', re.DOTALL)
    reCategoryDiv = re.compile('div class="b-category-list-inline-2">.*?</div>', re.DOTALL)
    reCategoryLi = re.compile('<li>.*?</li>', re.DOTALL)
    reDivText = re.compile('<div class="b-block-text__text">.*?</div>', re.DOTALL)
    reTextP = re.compile('<p>.*?</p>', re.DOTALL)
    reTextSpan = re.compile('<span>.*?</span>', re.DOTALL)
    reTag = re.compile('<.*?>', re.DOTALL)
    reSpace = re.compile('\s{2,}', re.DOTALL)

    dictInfo = {'autor':[], 'title':[], 'date':[], 'category':[], 'text':[], 'href':[]}

    for i in range(1, int(numPage())+1):
        if i == int(int(numPage())/3) or i == int(int(numPage())/3)*2:
            time.sleep(20) # Засыпание скрипта. Для того чтобы сервер постоянно отвечал
        print('Страница - ' + str(i))
        for x in range(len(artOnPage(i))):
            print('\tСтатья - ' + str(x+1))
            hrefPage = artOnPage(i)[x]
            href = inUrl(hrefPage)
            dictory = {'&nbsp;': '', '&raquo;': '»', '&laquo;': '«', '&ndash;': '-',
                       '&hellip;': '...', '&mdash;': ' — '}
            
            title = reTitle.search(href).group()
            title = reSpace.sub('', reTag.sub('', title))
            if reAutor.search(href) != None:
                autor = reAutor.search(href).group()
                autor = reSpace.sub('', reTag.sub('', autor))
            else:
                autor = 'Noname'
            date = reDate.findall(href)
            date = reSpace.sub('', reTag.sub('', date[1]))
            category = []
            if reCategoryDiv.search(href) != None:
                categoryDiv = reCategoryDiv.search(href).group()
                categoryLi = reCategoryLi.findall(categoryDiv)
                for cat in categoryLi:
                    category.append(reSpace.sub('', reTag.sub('', cat)))
            else:
                category.append('Nocategory')
            
            if reDivText.search(href) != None:
                divText = reDivText.search(href).group()
                text = reTextP.findall(divText)
                textAll = ''
                if len(text) > 0:
                    for tex in text:
                        textAll = textAll + reTag.sub('', reSpace.sub('', tex))+ '\n'

                        for it in dictory:
                            textAll = textAll.replace(it, dictory[it])
                else:
                    text = reTextSpan.findall(divText)
                    for tex in text:
                        textAll = textAll + reTag.sub('', reSpace.sub('', tex))+ '\n'

                        for it in dictory:
                            textAll = textAll.replace(it, dictory[it])
            else:
                textAll = 'NoText'

            dictInfo['autor'].append(autor)
            dictInfo['title'].append(title)
            dictInfo['date'].append(date)
            dictInfo['category'].append(category)
            dictInfo['text'].append(textAll)
            dictInfo['href'].append(hrefPage)
            category = []
    return dictInfo

def createFile():
    dic = infoArt()
    numArt = 1

    for i in range(len(dic['title'])):
        path = 'plain' + '\\' + dic['date'][i][6:10] + '\\' + dic['date'][i][3:5]
        if not os.path.isdir(path):
            os.makedirs(path)
        if not os.path.isdir('mystem-xml' + '\\' + dic['date'][i][6:10] + '\\' + dic['date'][i][3:5]):
            os.makedirs('mystem-xml' + '\\' + dic['date'][i][6:10] + '\\' + dic['date'][i][3:5])
        if not os.path.isdir('mystem-plain' + '\\' + dic['date'][i][6:10] + '\\' + dic['date'][i][3:5]):
            os.makedirs('mystem-plain' + '\\' + dic['date'][i][6:10] + '\\' + dic['date'][i][3:5])

        file = open(path + '\\art' + str(numArt) + '.txt', 'w+', encoding='utf-8')

        file.write(dic['text'][i])

        file.close()

        pText = os.getcwd() + '\\' + 'mystem-plain' + '\\' + dic['date'][i][6:10] + '\\' + dic['date'][i][3:5]
        pXml = os.getcwd() + '\\' + 'mystem-xml' + '\\' + dic['date'][i][6:10] + '\\' + dic['date'][i][3:5]
        pathM = os.getcwd() + '\\' + 'plain' + '\\' + dic['date'][i][6:10] + '\\' + dic['date'][i][3:5]

        os.system(os.getcwd() + '\\mystem.exe -cid ' + pathM + '\\art' + str(numArt) + '.txt' + ' ' + pText +
                  '\\art' + str(numArt) + '.txt')

        os.system(os.getcwd() + '\\mystem.exe -cid --format xml ' + pathM + '\\art' + str(numArt) + '.txt' + ' ' + pXml +
                  '\\art' + str(numArt) + '.xml')

        file = open(path + '\\art' + str(numArt) + '.txt', 'w+', encoding='utf-8')

        file.write('@au ' + dic['autor'][i] + '\n')
        file.write('@ti ' + dic['title'][i] + '\n')
        file.write('@da ' + dic['date'][i] + '\n')
        for cat in dic['category'][i]:
            file.write('@topic ' + cat + ' ')
        file.write('\n')
        file.write('@url ' + dic['href'][i] + '\n')

        file.write(dic['text'][i])

        file.close()

        numArt += 1
        
    for i in range(len(dic['title'])):
        file = open('metadata.csv', 'a+', encoding='utf-8')
        file.write(os.getcwd()+'\\plain\\'+ dic['date'][i][6:10] + '\\' + dic['date'][i][3:5]+'\\'
                   '\t'+dic['autor'][i]+'\t'+''+'\t'+''+'\t'+dic['title'][i]+'\t'+dic['date'][i]+
                   '\t'+'публицистика'+'\t'+''+'\t'+''+'\t'+dic['category'][i][0]+'\t'+''+'\t'+
                   'нейтральный'+'\t'+'н-возраст'+'\t'+'н-уровень'+'\t'+'общественно-политическая'+
                   '\t'+dic['href'][i]+'\t'+'Верный путь'+'\t'+''+'\t'+dic['date'][i][6:10]+'\t'+
                   'газета'+'\t'+'Россия'+'\t'+'Ординский район'+'\t'+'ru\n')
    file.close()      

def main():
    createFile()

if __name__ == "__main__":
    main()
