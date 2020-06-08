# 如果文件在当前同级，则直接写名字就可以
# 在widows中路径用\\或/或原始字符串r
f=open('aa')
# 读取文件的内容，会将内容全部保存为一个字符串返回
content=f.read()
print(content)
f.close()

# with...as 语句,可以自动结束
try:
    with open('aa') as f2:
        print(f2.read())
except Exception:
    print(Exception)
