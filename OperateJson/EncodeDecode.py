#  @Function:  测试json数据格式和python数据格式的互相转换
#  ＠Time:2020/5/21 下午3:31
#  @Author:Flank
import json

# 字典转json字符串
myDict = {
    'name': 'tom',
    'age': 18,
    'addr': 'ShangHai'
}
jsonStr = json.dumps(myDict)
print(type(jsonStr))

# Json字符串转字典
data2 = json.loads(jsonStr)
print(type(data2))

# 写json数据到文件
with open('data.json', 'w') as f:
    json.dump(myDict, f)

# 读取文件中的数据
with open('data.json', 'r') as f:
    tmpData = json.load(f)
    for k, v in tmpData.items():
        print(k, v)
