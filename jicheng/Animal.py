class Animal():
    def run(self,name):
        print(name,'动物会跑')
    def sleep(self):
        print('动物睡觉')

# 括号类就是当前类的父类
# 所有类的父类都是object
class Dog(Animal):
    def __init__(self,name):
        pass
    # 方法重写
    def sleep(self):
        print("狗睡觉")


# d=Dog()
# 父类中的所有方法都会被子类继承，包括特殊方法
d=Dog('斑点狗')
d.run('s')
d.sleep()
# isinstance()用来检查一个对象是否是一个类的实例
# 如果这个类是这个对象的父类，也会返回True

print(isinstance(d,Animal))