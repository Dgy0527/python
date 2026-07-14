'''
16、
题目简述
随着中国经济高速增长,人民生活水平不断提高,旅游成了起来越多家庭的重要生活方式,
经过调查每位游客出游一次可给当地带来1000元的收入,为了不断增加旅游人数,给当地带来更多的旅游收入,
某旅游地自2011年起取消了景区门票,以下是该地2011-2017年游客人次数据。

年份（年）	人次/万次
2011	    278
2012	    339
2013	    400
2014	    683
2015	    589
2016	    633
2017	    1024

现请你使用以下字典，设计一个如下的程序（参考程序说明）：

luyou={'count':7,
        'people':[
            {'year':'2011','youkes':278},
            {'year':'2012','youkes':339},
            {'year':'2013','youkes':400},
            {'year':'2014','youkes':683},
            {'year':'2015','youkes':589},
            {'year':'2016','youkes':633},
            {'year':'2017','youkes':1024},
        ]

}

程序说明
1.输入开始年份
2.输出2017年的游客人次比输入的开始年份游客人次的增长率
注:(计算公式:(2017年游客人次 - 输入年份的游客人次）/ 输入年份的游客人次 * 100)

样例输入
请输入开始年份:2011
样例输出
2011-2017年的游客人次增长率为:268.34532374100723%

'''

#参考答案
luyou={'count':7,
        'people':[
            {'year':'2011','youkes':278},
            {'year':'2012','youkes':339},
            {'year':'2013','youkes':400},
            {'year':'2014','youkes':683},
            {'year':'2015','youkes':589},
            {'year':'2016','youkes':633},
            {'year':'2017','youkes':1024},
        ]

}

year1=input('请输入开始年份:')

for person in luyou['people']:
    if person['year']==year1:
        num=(1024-person['youkes'])/person['youkes']*100
        print(year1+'-2017年的旅游人次增长率为:'+str(num)+'%')

'''
对上面代码的改进:

luyou = {
    'count': 7,
    'people': [
        {'year': '2011', 'youkes': 278},
        {'year': '2012', 'youkes': 339},
        {'year': '2013', 'youkes': 400},
        {'year': '2014', 'youkes': 683},
        {'year': '2015', 'youkes': 589},
        {'year': '2016', 'youkes': 633},
        {'year': '2017', 'youkes': 1024},
    ]
}

# 1. 增加年份输入校验（防止用户输入不在列表中的年份导致程序崩溃）
valid_years = [item['year'] for item in luyou['people']]

while True:
    year1 = input('请输入开始年份:').strip()
    if year1 in valid_years:
        break
    print('输入错误:输入的年份不在数据范围内(2011-2017),请重新输入！')

# 2. 动态获取 2017 年的数据，而不是直接硬编码 1024
youkes_start = 0
youkes_2017 = 0

for person in luyou['people']:
    if person['year'] == year1:
        youkes_start = person['youkes']
    if person['year'] == '2017':
        youkes_2017 = person['youkes']

# 3. 计算并输出
num = (youkes_2017 - youkes_start) / youkes_start * 100
print(year1 + '-2017年的游客人次增长率为:' + str(num) + '%')
'''
 