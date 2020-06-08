# 功能： 复制一张图片

img=open('3.png','rb')
imgNew=open('new.png','wb')
for content in img:
   imgNew.write(content)
img.close()
imgNew.close()