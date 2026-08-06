'''
7、题目简述

运动是最好的医生，能够为你的健康保驾护航。下表是小年最近一周的运动步长记录：
时间	步数
星期一	20000
星期二	15650
星期三	25005
星期四	15030
星期五	10041
星期六	20404
星期日	999




将以上信息存入如下字典中：
1.info = {
2.    'name': '小年',
3.    'count':7,
4.    'data': [
5.        {'time': '星期一', 'steps': 20000},
6.        {'time': '星期二', 'steps': 15650},
7.        {'time': '星期三', 'steps': 25005},
8.        {'time': '星期四', 'steps': 15030},
9.        {'time': '星期五', 'steps': 10041},
10.        {'time': '星期六', 'steps': 20404},
11.        {'time': '星期日', 'steps': 999},
12.    ]
13.}

要求输入时间，输出在该时间小年的运动步数

程序说明
1.输入时间(星期x)
2.输出小年的运动步数

样例输入
请输入时间(星期x):星期一
样例输出
小年在星期一的运动步数为20000步

'''

info={
    'name':'小年',
    'count':7,
    'data':[
        {'time':'星期一','steps':20000},
        {'time':'星期二','steps':15650},
        {'time':'星期三','steps':25005},
        {'time':'星期四','steps':15030},
        {'time':'星期五','steps':10041},
        {'time':'星期六','steps':20404},
        {'time':'星期日','steps':999},
    ]
}

time=input('请输入时间(星期x):')

for dic in info['data']:
    if dic['time']==time:
        print('小年在'+time+'的运动步数为'+str(dic['steps'])+'步')


'''
对上面代码的改进:

info = {
    'name': '小年',
    'count': 7,
    'data': [
        {'time': '星期一', 'steps': 20000},
        {'time': '星期二', 'steps': 15650},
        {'time': '星期三', 'steps': 25005},
        {'time': '星期四', 'steps': 15030},
        {'time': '星期五', 'steps': 10041},
        {'time': '星期六', 'steps': 20404},
        {'time': '星期日', 'steps': 999},
    ]
}

if __name__ == '__main__':
    target_day = input('请输入时间(星期x): ').strip()
    found = False

    for record in info['data']:
        if record['time'] == target_day:
            print(f"小年在{target_day}的运动步数为{record['steps']}步")
            found = True
            break

    if not found:
        print(f"未找到{target_day}的运动记录，请输入正确的星期（如：星期一）。")

'''