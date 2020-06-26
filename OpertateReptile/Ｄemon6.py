# @Function:request:get 和 post
# @Time: 2020/6/23 下午11:13
# @Authon: flank
import requests
import webbrowser  # 能自动打开网页
from urllib.request import urlretrieve
'''
post:往服务器发送数据
get:打开特定的网页
'''


def testGet():
    '''
    发送get请求
    :return:
    '''
    param = {"wd": "美国"}
    r = requests.get('http://www.baidu.com/s', params=param)
    print(r.url)
    webbrowser.open(r.url)


def testPost():
    data = {'firstname': '莫烦', 'lastname': '周'}
    r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
    print(r.text)

def testImage():
    '''
    上传图片
    :return:
    '''
    file = {'uploadFile': open('./Statics/tt.jpeg', 'rb')}
    r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
    print(r.text)

def testLogin():
    '''
    登陆
    １．登陆信息会保存到cookie中，先使用post方式进行登陆，在用ｇｅｔ方式使用cookiｅ获取登陆后的网页．
    ２．比如我用 requests.post + payload 的用户信息发给网页, 返回的 r 里面会有生成的 cookies 信息. 接着我请求去登录后的页面时
    使用 request.get, 并将之前的 cookies 传入到 get 请求. 这样就能已登录的名义访问 get 的页面了.
    :return:
    '''
    loadData={'username':'Morvan','password':'password'}
    r= requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=loadData)
    print(r.cookies.get_dict())
    r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
    print(r.text)

def testSession():
    '''
    使用session保持会话状态
    :return:
    '''
    session = requests.Session()
    payload = {'username': 'Morvan', 'password': 'password'}
    r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())
    r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
    print(r.text)

def downloadFileUseUrlretrieve():
    IMAGE_URL = "https://pics2.baidu.com/feed/63d0f703918fa0ec54361321935485e83c6ddb77.jpeg?token=113419e49ccf0b766f16c16720f398f4"
    urlretrieve(IMAGE_URL, './Statics/image1.png')

def downloadFileUseRequest():
    '''
    适合下载大文件
    :return:
    '''
    IMAGE_URL = "https://pics2.baidu.com/feed/63d0f703918fa0ec54361321935485e83c6ddb77.jpeg?token=113419e49ccf0b766f16c16720f398f4"
    r=requests.get(IMAGE_URL)
    with open('./Statics/image2.png','wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)


if __name__ == '__main__':
    # testGet()
    # testPost()
    # testImage()
    # testLogin()
    # testSession()
    # downloadFileUseUrlretrieve()
    downloadFileUseRequest()