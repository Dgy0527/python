'''
9、题目简述
深圳市统计局发布,深圳最近6年的GDP数据如下:
年份（年）	GDP(万亿)
2022	3.24
2021	3.07
2020	2.78
2019	2.7
2018	2.53
2017	2.33

现请你使用以下字典，设计一个如下的程序（参考程序说明）：

1.GDP={'years':6,
2.     'data':[{"year":2022,"amount":3.24},
3.               {"year":2021,"amount":3.07},
4.               {"year":2020,"amount":2.78},
5.               {"year":2019,"amount":2.7},
6.               {"year":2018,"amount":2.53},
7.               {"year":2017,"amount":2.33}
8.               ]
9.     }

程序说明
1.输入年份(限定2018-2022年之间)
2.输出该年的GDP增长幅度
3.计算公式:GDP增长幅度= 输入年份的GDP - 上一年的GDP(保留两位小数)

样例输入
请输入年份:2022
样例输出
2022深圳GDP增长幅度为:0.17万亿

'''

GDP={'years':6,
     'data':[{"year":2022,"amount":3.24},
             {"year":2021,"amount":3.07},
             {"year":2020,"amount":2.78},
             {"year":2019,"amount":2.7},
             {"year":2018,"amount":2.53},
             {"year":2017,"amount":2.33}
            ]
     }

growth_gdp=0
this_year_gdp=0
last_year_gdp=0

this_year=int(input('请输入年份:'))

for data in GDP['data']:
    if data['year']==this_year:
        this_year_gdp=data['amount']
    if data['year']==this_year-1:
        last_year_gdp=data['amount']
        growth_gdp=round(this_year_gdp-last_year_gdp,2)
print(this_year,'GDP增长幅度为:'+str(growth_gdp)+'万亿')


'''
对上面代码的改进:

GDP = {
    'years': 6,
    'data': [
        {"year": 2022, "amount": 3.24},
        {"year": 2021, "amount": 3.07},
        {"year": 2020, "amount": 2.78},
        {"year": 2019, "amount": 2.7},
        {"year": 2018, "amount": 2.53},
        {"year": 2017, "amount": 2.33}
    ]
}

# 将列表转为字典，方便快速查找
gdp_dict = {item['year']: item['amount'] for item in GDP['data']}

if __name__ == '__main__':
    try:
        year = int(input('请输入年份: '))
    except ValueError:
        print('输入错误，请输入整数年份。')
        exit()

    if year < 2018 or year > 2022:
        print('年份限定为2018-2022,请重新输入。')
        exit()

    if year not in gdp_dict or (year - 1) not in gdp_dict:
        print('该年份或上一年数据不存在，无法计算增长幅度。')
        exit()

    current_gdp = gdp_dict[year]
    last_gdp = gdp_dict[year - 1]
    growth = current_gdp - last_gdp

    print(f'{year}深圳GDP增长幅度为:{growth:.2f}万亿')

'''