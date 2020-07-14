# @Function:测试从sheet_reg中解析到Reg和索引
# @Time: 2020/7/9 下午5:30
# @Authon: flank
import re

if __name__ == "__main__":

    readFile = open("ipg/Sheet_reg.ipg", 'rb')
    Ｔag=0

    while True:
        content = readFile.readline()
        if "Prototypes".encode() in content:
            Tag=1
        if Tag==1:
            pass
        if not content:
            break
        print(content)
    readFile.close()
    print(Tag)
