fileName='aa'
# 1.小文件一次性读取完
try:
    with open(fileName) as file:
        content=file.read(2)
        content1 = file.read(2)
        print(content,content1,len(content))
except Exception:
    print(Exception)
    print(f'{fileName}文件不存在')


# 2.读取大文件分多次读
# 定义每次读取文件的字符大小
fileSize=2
# 存储文件的内容
content2=''
with open(fileName) as file1:
    while True:
        contentTmp=file1.read(fileSize)
        # 如果文件读取结束，返回空字符串跳出循环
        if not contentTmp:
            break
        else:
            content2+=contentTmp
print(content2)
# 3.循环读
with open(fileName) as file2:
    # 这样也是一行一行的读
    for t in file2:
        print('#####',t)