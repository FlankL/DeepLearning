# @Function:测试正则表达式
# @Time: 2020/7/9 上午10:37
# @Authon: flank
import  re
import os


str=" Object Output( List Out1) ;  //_GUI 125,28"
str2=" Object ( Variant NxtIndex) AXIReadReg:A( Variant Data, Variant Index) ;  //_GUI 65,56"
#
# updateStr=re.findall(r"(?<=[(])[^()]+\.[^()]+(?=[)])",str)
# print(updateStr)
print(str.split(" "))
print(str2.split(" "))
os.system('/media/lmx/5C5409DB5409B932/work/flank/tools/SimpleTools/flank2bit/v2bit')

var=123
os.environ['var']=str(var)  #environ的键值必须是字符串
os.system('echo $var')

