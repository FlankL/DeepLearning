# @Function:使用Beautiful去解析css，
# @Time: 2020/6/23 下午12:16
# @Authon: flank
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
month = soup.find_all('li', {'class': 'month'})
for m in month:
    print(m.get_text())
jan = soup.find('ul', {"class": 'jan'})
d_jan = jan.find_all('li')  # use jan as a parent
for d in d_jan:
    print(d.get_text())
