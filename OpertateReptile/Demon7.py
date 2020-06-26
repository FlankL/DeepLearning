# @Function: 爬去鞠婧祎图片
# @Time: 2020/6/24 下午2:44
# @Authon: flank
import requests
from bs4 import BeautifulSoup
URL="https://baike.baidu.com/item/%E9%9E%A0%E5%A9%A7%E7%A5%8E/10201840#3"

html=requests.get(URL).text
with open('./test.html','wb')as f:
    f.write(html.encode())
soup=BeautifulSoup(html,'lxml')
imgURL=soup.find_all('a',{'class':'image-link'})
print("img nums:",len(imgURL))
for img in imgURL:
   url=img['src']
   r=requests.get(url,stream=True)
   imgName=url.split("/")[-1]
   with open("./Statics/鞠婧祎/%s"%imgName,'wb') as f:
       for chunk in r.iter_content(chunk_size=32):
           f.write(chunk)