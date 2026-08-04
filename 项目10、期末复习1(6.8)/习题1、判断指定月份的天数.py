month=int(input('请输入月份(1-12):'))
if month==2:
    days='28天或29天'
elif month in [4,6,9,11]:
    days='30天'
else:
    days='31天'
print('你输入的月份天数是:',days)


#超出月份
month=int(input('请输入月份(1-12):'))
if month==2:
    days='28天或29天'
elif month in [4,6,9,11]:
    days='30天'
elif month in [1,3,5,7,8,10,12]:
    days='31天'
else:
    print('请输入正确的月份')
    exit()
print('你输入的月份天数是:',days)

或者

month=int(input('请输入月份(1-12):'))
days='' #先初始化
if month==2:
    days='28天或29天'
elif month in [4,6,9,11]:
    days='30天'
elif month in [1,3,5,7,8,10,12]:
    days='31天'
else:
    print('请输入正确月份')
print('你输入的月份天数是:',days if days else '无效')





'''
对上面代码的改进:

1、仅月份判断,不引入年份

def get_days_by_month(month):
    if not 1 <= month <= 12:
        return None
    # 使用字典映射
    days_map = {
        1: 31, 2: '28或29', 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return days_map[month]

try:
    month = int(input('请输入月份(1-12): '))
    days = get_days_by_month(month)
    if days is None:
        print('输入的月份无效,请输入1-12之间的整数。')
    else:
        if month == 2:
            print(f'2月份的天数为:{days}(平年28天,闰年29天)')
        else:
            print(f'你输入的月份天数是：{days}天')
except ValueError:
    print('输入错误，请输入有效的整数。')


2、加入年份,用来判断闰年

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

try:
    month = int(input('请输入月份(1-12): '))
    if not 1 <= month <= 12:
        print('月份必须在1-12之间。')
    else:
        year = int(input('请输入年份(如2026): '))
        days = get_days(month, year)
        print(f'{year}年{month}月有{days}天。')
except ValueError:
    print('输入错误，请输入整数。')

'''