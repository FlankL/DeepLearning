import os #导入包含文件操作的内置os模块
from pprint import pprint # 让打印更好看

r=os.listdir() #获取指定目录结构。
r=os.getcwd() #获取当前所在的目录
pprint(r)