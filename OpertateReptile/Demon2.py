# @Function:使用BeautifulSoup解析网页
# @Time: 2020/6/23 上午11:46
# @Authon: flank
from bs4 import BeautifulSoup
from urllib.request import urlopen
html=urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
soup=BeautifulSoup(html,features='lxml')
print(soup.h1)

allHref=soup.find_all('a')
allHref=[l['href'] for l in allHref]
print('\n',allHref)