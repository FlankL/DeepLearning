a=10
b=10
def test():
    print('this is a test ')
class Person():
    def __init__(self):
        pass

# 测试代码，只有当当前模块作为主模块的时候才需要执行，而模块被其他模块引入时，不需要执行的
# 所以需要检查当前模块是否是主模块
if __name__=='__main__':
    print(a)