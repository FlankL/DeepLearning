# s={1,2,3,4,5}
# s1={3,4,5,6,7}
# #& 交集运算
# print(s & s1)
# # | 并集运算
# print(s | s1)
# # -差集
# print(s-s1)
# print(s1-s)
# # ^ 异或集:获取只在一个集合中出现的元素。
# print(s ^ s1)
# # <= 检查一个集合是否是另一个集合的子集（如果一个集合中的元素 全部都在另一个集合中出现，那么这个集合就是另一个集合的子集。）
# print(s<=s1)
# # < 检查一个集合是否是另一个集合的真子集（s1含有s的所有元素，s1还有s中没有的元素）
# print(s<s1)
def test1(c, *a, b):
    print(c, a, b, type(a))


def test2(**d):
    print(d, type(d))


def test3(a, b, c):
    print(a, b, c)


test1(10, 1, 3, 4, b=6)
test2(a=1, b=2, c=3)
myList = list('hel')

test3(*myList)
