#首先用sort()排序，然后用del删除第一个元素和最后一个元素
import random

num_list=[] #一个选手的分数
columns=10 #10个裁判

for j in range(columns):
    num=random.randint(0,10) #随机生成0-10之间的一个整数
    num_list.append(num) #添加到选手列表中
print(num_list)

num_list.sort() #对列表进行升序排序
print(num_list)

del num_list[0] #删除第一个元素
del num_list[-1] #删除最后一个元素
print(num_list)



'''
对上面代码的改进:

import random

def calculate_final_score(num_judges=10, min_score=0, max_score=10, decimals=1):
    """
    模拟评分：生成 num_judges 个裁判的分数，去掉最高分和最低分后计算平均分。
    """
    if num_judges < 3:
        raise ValueError("裁判人数至少为3人,才能去掉最高分和最低分。")

    # 生成随机分数（支持小数）
    scores = [round(random.uniform(min_score, max_score), decimals) for _ in range(num_judges)]
    print(f"原始分数: {scores}")

    # 排序
    sorted_scores = sorted(scores)
    # 去掉最高分和最低分（使用切片）
    middle_scores = sorted_scores[1:-1]
    print(f"去掉最高分和最低分后: {middle_scores}")

    # 计算平均分
    if middle_scores:  # 非空
        final_score = sum(middle_scores) / len(middle_scores)
        final_score = round(final_score, decimals)
        print(f"最终得分: {final_score}")
        return final_score
    else:
        # 理论上不会走到这里，因为 num_judges >= 3
        return None

# 示例调用
if __name__ == "__main__":
    calculate_final_score(num_judges=10)

'''