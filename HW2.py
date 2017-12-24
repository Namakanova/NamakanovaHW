import urllib.request
from lxml import etree
from io import StringIO
import matplotlib.pyplot as plt

url = 'http://wiki.dothraki.org/Vocabulary'  # адрес страницы, которую мы хотим скачать
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'  # хотим притворяться браузером

req = urllib.request.Request(url, headers={'User-Agent': user_agent})
# добавили в запрос информацию о том, что мы браузер Мозилла



with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

parser = etree.HTMLParser(remove_blank_text=True, remove_comments=True)
tree = etree.parse(StringIO(html), parser)
root = tree.getroot()
row_data = []
data = {}
parts_of_s = {}
letters = {}

for child in root[1][0][0][0][2]:
    if child.tag == 'ul' or child.tag == 'dl':
        row_data.append(child)

row_data = row_data[:len(row_data) - 3]

for i in range(len(row_data)):
    if row_data[i].tag == 'ul':
        data[row_data[i][0].findtext('b')] = str(row_data[i + 1][0].findtext('i')).replace('.', '').replace('\'',
                                                                                                            '').strip()

for elem in data:
    if data[elem] in parts_of_s:
        parts_of_s[data[elem]] += 1
    else:
        parts_of_s[data[elem]] = 1

# Some data prep
parts_of_s.pop('None')
parts_of_s.pop('part')
parts_of_s.pop('phrase')
parts_of_s.pop('np')
parts_of_s.pop('det')
parts_of_s['adv'] += parts_of_s.pop('conj adv') + parts_of_s.pop('loc adv')
parts_of_s['prep'] += parts_of_s.pop('prep→abl') + parts_of_s.pop('prep→all') + parts_of_s.pop(
    'prep→gen') + parts_of_s.pop('prep→nom')
parts_of_s['ni'] += parts_of_s.pop('ni/na')
parts_of_s['dem'] = parts_of_s.pop('dem adj') + parts_of_s.pop('dem pn')
parts_of_s.pop('dem')
parts_of_s['prop n'] += parts_of_s.pop('propn')
parts_of_s['v'] += parts_of_s.pop('v aux') + parts_of_s.pop('v→abl')
parts_of_s['vtr'] += parts_of_s.pop('vtr→abl')


plt.figure(figsize=(12, 5))
plt.bar(range(len(parts_of_s)), list(parts_of_s.values()), align='center')
plt.xticks(range(len(parts_of_s)), list(parts_of_s.keys()))
plt.show()


for word in data.keys():
    if str(word).lower()[0] in letters:
        letters[str(word).lower()[0]] += 1
    else:
        letters[str(word).lower()[0]] = 1

plt.figure(figsize=(15, 5))
plt.bar(range(len(letters)), list(letters.values()), align='center')
plt.xticks(range(len(letters)), list(letters.keys()))
plt.show()