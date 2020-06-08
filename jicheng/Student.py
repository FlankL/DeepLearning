# 创建一个类
class Student():
    # 特殊方法都是以__开头，__结尾的方法
    # 特殊方法不需要我们自己调用
    def __init__(self, name):
        self.__name = name

    def __run(self):
        print(self.__name, "run")

    def say(self):
        self.__run()
        print(self.__name, 'say')

    # def getName(self):
    #     return self.__name
    #
    # def setName(self, name):
    #     self.__name = name

    # 使用装饰器来简写getter(),setter()方法
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

s1 = Student('tom')
# 通过get ,set获取属性
# print(s1.getName())
s1.name='jack'
print(s1.name)
s1.say()
