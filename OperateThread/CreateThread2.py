#  @Function: 创建线程, 方法二
# 　＠Time:2020/5/21 下午4:42
#  @Author:Flank

from threading import Thread
import time


# 继承Thread类
class SayHi(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print(f'{self.name} say Hi')


if __name__ == '__main__':
    t = SayHi('hh')
    t.start()
    print('主线程')
