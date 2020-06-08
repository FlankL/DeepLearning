#  @Function: numpy的数据类型
#　＠Time:2020/6/1 下午1:56
#  @Author:Flank
import numpy as np
# 1.创建一个指定类型的变量
var_uint8=np.uint8(10)
print(var_uint8,var_uint8.dtype)
# 2.通过astype()转换数组元素的数据类型
array1=np.arange(12).reshape(3,4)
print("转换前:",array1.dtype)
# 转换成float32
floatArr=array1.astype(np.float32)
print("转换成float32:",floatArr.dtype)
stringArr=array1.astype(np.str)
print("转换成str",stringArr.dtype)