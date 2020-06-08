#  @Function: 创建线程, 方法一
# 　＠Time:2020/5/21 下午4:42
#  @Author:Flank

from threading import Thread
import time



def sayHi(name):
    time.sleep(2)
    print(f'{name} say hello')


if __name__ == '__main__':
    thread1 = Thread(target=sayHi, args=('xiaomign',))
    thread1.start()
    print('主线程')
