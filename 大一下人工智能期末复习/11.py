'''

某公司举办答谢客户活动，每位客户都有唯一编号，用一个列表存放如下图所示。
每次输入一个幸运种子数，如果客户编号能够被种子数整除的话，则该编号就是幸运编号，该客户就可以获得一定奖品，也有可能没有幸运编号。

1.list1 = [254, 365, 879, 747, 476, 878, 555, 647, 254, 474]

程序说明
1.输入一个种子数
2.输出列表中所有能够被种子数整除的幸运编号数据

样例输入
请输入一个种子数:3
样例输出
幸运编号: 879
幸运编号: 747
幸运编号: 555
幸运编号: 474

'''

list1=[254,365,879,747,476,878,555,647,254,474]

max1=eval(input('请输入一个种子数:'))

flag=0

for i in list1:
    if i%max1==0:
        print('幸运编号:',i)
        flag=1

if flag==0:
    print('没有幸运编号')


'''
对上面代码的改进:

customer_ids = [254, 365, 879, 747, 476, 878, 555, 647, 254, 474]

if __name__ == '__main__':
    try:
        seed = int(input('请输入一个种子数: '))
    except ValueError:
        print('输入错误，请输入一个整数种子数。')
        exit()

    if seed == 0:
        print('种子数不能为0,请重新运行程序。')
        exit()
    # 如果业务上允许负数，可以不加此判断；这里假设种子数为正整数
    if seed < 0:
        print('种子数应为正整数。')
        exit()

    found = False
    for customer_id in customer_ids:
        if customer_id % seed == 0:
            print(f'幸运编号: {customer_id}')
            found = True

    if not found:
        print('没有幸运编号')

'''