#  @Function: 一个计算器的可执行程序
#　＠Time:2020/5/25 22:23
#  @Author:Flank


print("welcom to use My calctor")

while True:
    exp=input('请输入计算值表达式[quit退出]')
    if exp =='quitL':
        break
    try:
       result=eval(exp)
    except:
        print('无效表达式')
        continue
    print('result:',result)