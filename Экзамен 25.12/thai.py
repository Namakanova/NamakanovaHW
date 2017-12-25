from lxml import etree
import os

data = {}
parser = etree.HTMLParser(remove_blank_text=True, remove_comments=True)
directory = os.getcwd() + '/thai_pages'
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        file = os.getcwd() + '/thai_pages/' + filename
        tree = etree.parse(file, parser)
        root = tree.getroot()
        try:
            for child in root[1].find(".//div[@id='tl-content']")[4][0][-1]:
                if (len(child[0]) and len(child) > 3):
                    k = child[0].findtext('a')
                    v = child[3].text
                    data[k] = v
        except Exception:
            continue
    else:
        continue

print(data)

new_data = {}
for elem in data:
    new_data[data[elem]] = elem

print(new_data)
