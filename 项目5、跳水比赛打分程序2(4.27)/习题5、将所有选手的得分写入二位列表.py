#将所有选手的得分写入二位列表
import random

dic={'s01':3.1,'s02':3.1,'s03':3.1,'s04':3.1,'s05':3.1,'s06':3.1,'s07':3.1,'s08':3.1}

num_list=[] #一个选手的分数
result_list=[] #所有选手的得分
rows=8 #8个选手
columns=10 #10个裁判

for i in range(rows):
    num_list.append([])
    result_list.append([])

    for j in range(columns):
        num=random.randint(0,10) #随机生成0-10之间的一个整数
        num_list[i].append(num) #添加到选手列表中

    num_list[i].sort #对列表进行升序排序
    del num_list[i][0] #删除第一个元素
    del num_list[i][-1] #删除最后一个元素

    aver=round(sum(num_list[i])/len(num_list[i]),2) #求列表的平均值
    scor=round(aver*dic['s0'+str(i+1)],2) #求最后得分

    result_list[i].append('s0'+str(i+1))
    result_list[i].append(aver)
    result_list[i].append(dic['s0'+str(i+1)])
    result_list[i].append(scor)
    print(result_list[i])
    


'''
对上面代码的改进:

import random

# 选手难度系数
difficulty = {
    's01': 3.1, 's02': 3.1, 's03': 3.1, 's04': 3.1,
    's05': 3.1, 's06': 3.1, 's07': 3.1, 's08': 3.1
}

PLAYER_COUNT = 8
JUDGE_COUNT = 10

# 预分配二维列表
all_scores = []      # 原始分数（可选保留）
result_list = []     # 最终结果：[选手ID, 平均分, 难度系数, 最后得分]

for i in range(PLAYER_COUNT):
    pid = f's0{i+1}'          # 选手ID
    # 生成10个裁判的随机分数
    scores = [random.randint(0, 10) for _ in range(JUDGE_COUNT)]
    all_scores.append(scores)  # 保留原始分数

    # 排序并去掉最高分和最低分（不修改原始列表）
    sorted_scores = sorted(scores)
    trimmed = sorted_scores[1:-1]   # 去掉一个最高和一个最低

    avg_score = round(sum(trimmed) / len(trimmed), 2)
    final_score = round(avg_score * difficulty[pid], 2)

    result_list.append([pid, avg_score, difficulty[pid], final_score])

# 打印最终结果
print("选手成绩列表：")
for row in result_list:
    print(f"ID: {row[0]}, 平均分: {row[1]}, 难度系数: {row[2]}, 最后得分: {row[3]}")

# 如果需要二维列表完整内容
print("\n完整二维列表:")
print(result_list)

'''