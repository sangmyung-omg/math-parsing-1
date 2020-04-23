from bs4 import BeautifulSoup
import pandas as pd
import re

uk_data = []
property_data = []

book1_1 = open('./풍산자/2-1.xml', 'r', 
            encoding='utf-8')
xml = book1_1.read()
soup = BeautifulSoup(xml, 'xml')
terms = soup.findAll('P')
uks = []

for term in terms:
    p = re.compile(r'[가-힣]: ')
    term = re.sub('<.+?>', '', str(term), 0).strip()
    m = p.search(term)
    if m:
        uks.append(term)

def_uk = []
def_ex = []

for uk in uks:
    p = re.compile(r':')
    m = p.search(uk)
    if m:
        def_uk.append(uk[2:m.start()])
        def_ex.append(uk[m.end()+1:])
    
dictionary = dict(zip(def_uk, def_ex))
df = pd.DataFrame(data=dictionary, index=[0])
df = (df.T)
df.to_excel('2-1.xlsx')


# 수정
a = 1