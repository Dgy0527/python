'''
1、根据出生年份和当前年份,计算年龄。
2、首先需要判断用户输入的出生年份是否是整数,如果不是整数,提示"输入有误,出生年份必须是整数"
3、如果用户输入的是整数,那计算用户的年龄并输出"您的年龄是xx"
'''

year=eval(input('请输入出生年份:'))

if isinstance(year,int):
    nianling=2026-year
    print('你的年龄是:',nianling,'岁')
else:
    print('输入有误,出生年份必须是整数')


'''
对上面代码的改进:

from datetime import date

user_input = input('请输入出生年份:')

try:
    birth_year = int(user_input)          # 直接尝试转整数，失败则说明非整数
except ValueError:
    print('输入有误,出生年份必须是整数')
else:
    current_year = date.today().year      # 动态获取今年年份
    if birth_year > current_year:
        print('出生年份不能大于当前年份！')
    elif birth_year < 1900:               # 可根据需要调整下限
        print('请输入合理的出生年份(如1900年之后)')
    else:
        age = current_year - birth_year
        print(f'您的年龄是{age}')          # 严格按题目要求输出

'''