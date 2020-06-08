try:
    print(10/0)
except Exception as e:
    print('出错了' ,e,type(e))