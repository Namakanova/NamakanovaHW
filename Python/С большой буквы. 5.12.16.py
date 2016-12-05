with open('text.txt', "r", encoding = "utf-8") as f: 
    s = f.read()
    s = s.replace("\n"," ")
    words = s.split()
count_cap = 0
count_total = len (words)
for  words in words: 
    if words[0].isupper(): 
        count_cap +=1
print ("Процент слов с большой буквы" , ( count_cap / count_total) * 100)
