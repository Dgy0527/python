'''
12、题目简述

随着中国经济的蓬勃发展,中国旅游行业在2019年之前也一直处于快速上升的态势,并在2019年达到顶峰。
疫情的出现对我国旅游业造成重创,但在疫情结束后开始回暖。以下表格是2017-2023年国内旅游数据情况:

年份（年）	旅游总人次（万）
2017	   488765.5
2018	   553911.5
2019	   600609.9
2020	   287900.4
2021	   324623.2
2022	   253789.9
2023	   455579.2(预估)

现请你使用以下字典，设计一个如下的程序（参考程序说明）：
1.passenger = {
2.    'count': 7,
3.    'people': [
4.        {'year': '2017', 'passengers': 488765.5},
5.        {'year': '2018', 'passengers': 553911.5},
6.        {'year': '2019', 'passengers': 600609.9},
7.        {'year': '2020', 'passengers': 287900.4},
8.        {'year': '2021', 'passengers': 324623.2},
9.        {'year': '2022', 'passengers': 253789.9},
10.        {'year': '2023', 'passengers': 455579.2},
11.    ]
12.}

程序说明
1.输入计算年份
2.输出该年份相比于2019年的旅游人次比例
注：(计算公式：输入年份的旅游人次 / 2019年的旅游人次 * 100)

样例输入
请输入开始年份:2023
样例输出
2023年国内旅游总人次为2019年的75.85276233%

'''

passenger = {
    'count': 7,
    'people': [
        {'year': '2017', 'passengers': 488765.5},
        {'year': '2018', 'passengers': 553911.5},
        {'year': '2019', 'passengers': 600609.9},
        {'year': '2020', 'passengers': 287900.4},
        {'year': '2021', 'passengers': 324623.2},
        {'year': '2022', 'passengers': 253789.9},       
        {'year': '2023', 'passengers': 455579.2},
    ]
}

year1=input('请输入计算年份:')

for person in passenger['people']:
    if person['year']==year1:
        num=person['passengers']/600609.9*100
        print(year1+'年国内旅游总人次为2019年的'+str(num)+'%')


'''
对上面代码的改进:

passenger = {
    'count': 7,
    'people': [
        {'year': '2017', 'passengers': 488765.5},
        {'year': '2018', 'passengers': 553911.5},
        {'year': '2019', 'passengers': 600609.9},
        {'year': '2020', 'passengers': 287900.4},
        {'year': '2021', 'passengers': 324623.2},
        {'year': '2022', 'passengers': 253789.9},
        {'year': '2023', 'passengers': 455579.2},
    ]
}

# 1. 先找出2019年的数据(动态获取)
base_year = '2019'
base_value = None
for item in passenger['people']:
    if item['year'] == base_year:
        base_value = item['passengers']
        break

if base_value is None:
    print(f"错误：字典中未找到{base_year}年的数据")
    exit()

# 2. 获取用户输入并去除可能的前后空格
year_input = input("请输入开始年份:").strip()

# 3. 查找输入年份的数据
target_value = None
for item in passenger['people']:
    if item['year'] == year_input:
        target_value = item['passengers']
        break

# 4. 处理无效年份
if target_value is None:
    print(f"错误：未找到{year_input}年的数据,请重新输入有效年份(2017-2023)")
else:
    # 5. 计算比例并格式化保留8位小数
    ratio = target_value / base_value * 100
    print(f"{year_input}年国内旅游总人次为{base_year}年的{ratio:.8f}%")

'''