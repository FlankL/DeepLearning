# @Function: 爬虫的helloworld
# @Time: 2020/6/23 上午10:19
# @Authon: flank
from urllib.request import urlopen #导入urllib
import re #导入正则表达式库

html=urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
res=re.findall(r"<title>(.+?)</title>",html)# 使用正则表达式进行筛选
res1=re.findall(r"<p>(.*?)</p>",html,flags=re.DOTALL)#DOTALL 表示匹配多行
res2=re.findall(r'href="(.*?)"',html)
print('title',res[0])
print('p',res1[0])
print("href",res2)

# print(html)
