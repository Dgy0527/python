#将选手的得分写入Excel文件
import random
from openpyxl import Workbook #导入写模块

dic={'s01':3.1,'s02':3.1,'s03':3.1,'s04':3.1,'s05':3.1,'s06':3.1,'s07':3.1,'s08':3.1,}

num_list=[] #一个选手的分数
columns=10 #10个裁判

for j in range(columns):
    num=random.randint(0,10) #随机生成0-10之间的一个整数
    num_list.append(num) #添加到选手列表中
print(num_list)

num_list.sort() #对列表进行升序
print(num_list)

del num_list[0] #删除第一个元素
del num_list[-1] #删除最后一个元素
print(num_list)

aver=round(sum(num_list)/len(num_list),2) #求列表的平均值
scor=round(aver*dic['s01'],2) #求最后得分
print(aver)
print(scor)

#开始写入代码
wb=Workbook()
sheet=wb.active
sheet.title='成绩表'
sheet_field=['选手ID','姓名','国家','难度系数','平均分','最后得分','名次']
sheet.append(sheet_field)
sheet['A2']='s01'
sheet['B2']='马丁'
sheet['C2']='意大利'
sheet['D2']=dic.get('s01')
sheet['E2']=aver
sheet['F2']=scor
wb.save('result.xlsx')


'''
对上面代码的改进:

import random
from openpyxl import Workbook

# 选手信息列表（可自由扩展）
players = [
    {'ID': 's01', '姓名': '马丁', '国家': '意大利', '难度系数': 3.1},
    {'ID': 's02', '姓名': '玛丽', '国家': '法国', '难度系数': 3.4},
    {'ID': 's03', '姓名': '杰克', '国家': '美国', '难度系数': 3.0},
]

# 生成分数并计算最终得分
results = []
for player in players:
    # 10名裁判打分(0~10随机整数)
    scores = [random.randint(0, 10) for _ in range(10)]
    scores.sort()               # 升序排列
    trimmed = scores[1:-1]      # 去掉最高分和最低分
    avg_score = round(sum(trimmed) / len(trimmed), 2)
    final_score = round(avg_score * player['难度系数'], 2)
    results.append({
        '选手ID': player['ID'],
        '姓名': player['姓名'],
        '国家': player['国家'],
        '难度系数': player['难度系数'],
        '平均分': avg_score,
        '最后得分': final_score,
    })

# 按最后得分降序排名（同分可并列，这里简单处理）
results.sort(key=lambda x: x['最后得分'], reverse=True)
for rank, r in enumerate(results, start=1):
    r['名次'] = rank

# 写入 Excel
wb = Workbook()
sheet = wb.active
sheet.title = '成绩表'

# 写入表头
fields = ['选手ID', '姓名', '国家', '难度系数', '平均分', '最后得分', '名次']
sheet.append(fields)

# 写入数据行
for r in results:
    sheet.append([r[f] for f in fields])

wb.save('result.xlsx')
print("成绩表已生成:result.xlsx")

'''