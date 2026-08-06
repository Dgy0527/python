'''
8、题目简述
2023年深圳市马拉松比赛如期举行,全程42.195公里,共有2500余人报名参与。
项目组委会为参赛选手准备了丰厚的奖金，只要跑完全程的选手都可以获得现金奖励，具体数额见下表：

完成时间（分钟）	奖金数额（元）
<=150	           15000
<=200	           10000
<=250	           5000
<=300	           1000
>350	           100

程序说明
1.输入选手完成马拉松的时间
2.输出该选手可以获得的奖金数额

样例输入
请输入选手完成马拉松的时间(分钟):165
样例输出
该选手获得的奖金数额为:10000元

'''

time=eval(input('请输入选手完成马拉松的时间(分钟):'))
money=0

if time<=150:
    money=15000
elif time<=200:
    money=10000
elif time<=250:
    money=5000
elif time<300:
    money=1000
else:
    money=100
print('该选手获得的奖金数额为:'+str(money)+'元')


'''
对上面代码的改进:

if __name__ == '__main__':
    try:
        finish_time = int(input('请输入选手完成马拉松的时间(分钟): '))
        if finish_time < 0:
            raise ValueError('时间不能为负数')
    except ValueError as e:
        print(f'输入错误：{e}，请输入一个非负整数。')
        exit()

    if finish_time <= 150:
        money = 15000
    elif finish_time <= 200:
        money = 10000
    elif finish_time <= 250:
        money = 5000
    elif finish_time <= 300:
        money = 1000
    elif finish_time > 350:
        money = 100
    else:  # 300 < finish_time <= 350
        money = 0   # 题目未提及该区间的奖金,这里设为0或给予提示

    if money > 0:
        print(f'该选手获得的奖金数额为:{money}元')
    else:
        print('很遗憾，您未达到获得奖金的时限要求。')

'''