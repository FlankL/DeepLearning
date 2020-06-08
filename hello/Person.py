class Person():

    # 定义一个类方法
    @classmethod
    def myClass(cls):
        print('这是ｍyClass',cls)

    # 定义一个对象方法
    def fun1(self):
       print('this is fun1')

    # 定义一个静态方法
    @staticmethod
    def fun2():
        print('this is method function')
p1=Person()
p1.myClass()
