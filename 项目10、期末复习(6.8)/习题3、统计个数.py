#从键盘反复输入正数,统计输入的正数个数

'''
#这是什么东西？

count=0
num=float(input('请输入一个正数(不是正数就退出输入):'))

while num >0:
    print('输入的数是正数')
    count+=1
    print('总个数是',count)

while num==0:
    print('输入的数是0,不是正数')

while num<0:
    print('输入的数不是正数')
'''

count=0
while True:
    num=float(input('请输入一个正数(不是正数就退出输入):'))
    if num>0:
        count+=1
    else:
        break
print('共输入的正数个数是',count,'个')


'''
对上面代码的改进:

count = 0
while True:
    try:
        num = float(input('请输入一个正数(输入0或负数结束):'))
    except ValueError:
        print('输入无效，请输入数字！')
        continue

    if num > 0:
        count += 1
        print(f'当前为正数，已累计 {count} 个')
    else:
        print('输入非正数，结束输入。')
        break

print(f'共输入的正数个数是：{count} 个')

'''