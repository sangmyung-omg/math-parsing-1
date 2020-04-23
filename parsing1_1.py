from bs4 import BeautifulSoup
import pandas as pd
import re

uk_data = []
property_data = []

book = open('./풍산자/1-1.xml', 'r', 
            encoding='utf-8')
xml = book.read()
soup = BeautifulSoup(xml, 'xml')
uks = soup.findAll('_00-개념1.') # 66개
properties = soup.findAll('_00-개념본문') # 200개

for uk, property in zip(uks, properties):
    tmp = re.sub('<.+?>', '', str(uk), 0).strip()
    tmp = re.sub('\d[.\t]', '', tmp, 0).strip()
    tmp = re.sub('\u2009', '', tmp, 0).strip()
    uk_data.append(tmp)
    tmp = re.sub('<.+?>', '', str(property), 0).strip()
    tmp = re.sub(r'\u200c', '', tmp, 0).strip()
    property_data.append(tmp)
    
def_uk = []
def_ex = []

for property in property_data:
    p = re.compile(r':')
    m = p.search(property)
    if m:
        def_uk.append(property[2:m.start()])
        def_ex.append(property[m.end()+1:])
    
dictionary = dict(zip(def_uk, def_ex))
df = pd.DataFrame(data=dictionary, index=[0])
df = (df.T)
df.to_excel('1-1.xlsx')