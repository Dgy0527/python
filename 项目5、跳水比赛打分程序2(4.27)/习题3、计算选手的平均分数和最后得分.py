#用SUM()对列表除以LEN()列表的元素个数等于平均分,最后得分平均分乘以难度系数
import random

dic={'s01':3.1,'s02':3.1,'s03':3.1,'s04':3.1,'s05':3.1,'s06':3.1,'s07':3.1,'s08':3.1}

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

aver=round(sum(num_list)/len(num_list),2) #求列表的平均值
scor=round(aver*dic['s01'],2) #求最后得分
print(aver)
print(scor)



'''
对上面代码的改进:

import random

# 难度系数字典（键为选手编号，值为难度系数）
difficulty_dict = {
    's01': 3.1, 's02': 3.1, 's03': 3.1, 's04': 3.1,
    's05': 3.1, 's06': 3.1, 's07': 3.1, 's08': 3.1
}

def calculate_final_score(judge_count, difficulty_coefficient):
    """
    生成裁判评分，去掉最高分和最低分，计算平均分后乘以难度系数。
    """
    if judge_count < 3:
        raise ValueError("裁判人数至少为3人,才能去掉最高分和最低分。")

    # 生成随机分数(0~10之间的整数)
    scores = [random.randint(0, 10) for _ in range(judge_count)]
    print(f"原始分数: {scores}")

    # 排序并去掉最高分和最低分（使用切片，更安全）
    scores.sort()
    middle_scores = scores[1:-1]  # 直接取出中间部分
    print(f"去掉最高分和最低分后: {middle_scores}")

    # 计算平均分（保证列表不为空）
    average_score = round(sum(middle_scores) / len(middle_scores), 2)
    print(f"平均分: {average_score}")

    # 最终得分 = 平均分 * 难度系数
    final_score = round(average_score * difficulty_coefficient, 2)
    print(f"最终得分: {final_score}")
    return final_score

# 示例调用：计算选手 s01 的得分
if __name__ == "__main__":
    calculate_final_score(
        judge_count=10,
        difficulty_coefficient=difficulty_dict['s01']
    )


'''