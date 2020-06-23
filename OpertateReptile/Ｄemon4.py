# @Function:在BeautifulSoup中使用正则表示式
# @Time: 2020/6/23 下午2:25
# @Authon: flank
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
soup=BeautifulSoup(html,features='lxml')
imgLinks=soup.find_all('img',{"src":re.compile('.*?\.jpg')})#.*? 表示匹配任何形式的链接，．jpg表示匹配ｊｐｇ图片
a=soup.find_all('a',{'href':re.compile('https://morvan.*')})# 匹配以这个开头的连接
for link in imgLinks:
    print(link['src'])
for link in a:
    print(link['href'])