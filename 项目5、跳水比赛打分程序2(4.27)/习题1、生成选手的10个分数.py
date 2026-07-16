#10个裁判给一个选手打分
import random 

num_list=[] #一个选手的分数
columns=10 #10个裁判

for j in range(columns):
    num=random.randint(0,10) #随机生成0-10之间的一个整数
    num_list.append(num) #添加到选手列表中
print(num_list)



'''
上面代码存在的问题:1、没有计算选手的总分
                  2、没有去掉最高分和最低分
对上面代码的改进:

import random

# 提取常量
NUM_JUDGES = 10
MIN_SCORE = 0
MAX_SCORE = 10

# 生成 10 个随机分数
scores = [random.randint(MIN_SCORE, MAX_SCORE) for _ in range(NUM_JUDGES)]

print(f"10位裁判的打分:{scores}")

# 核心逻辑：去掉最高分和最低分
scores.remove(max(scores))
scores.remove(min(scores))

# 计算最终得分
final_score = sum(scores) / len(scores)

# 输出结果
print(f"去掉最高分和最低分后：{scores}")
print(f"该选手的最终得分是：{final_score:.2f} 分")

'''