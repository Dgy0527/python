'''
定义字典grades,元素对分别为 语文 90,数学 88,英语 75,体育 80
使用for循环输出成绩大于81的科目和对应的成绩
'''

'''
#我的

grades={'语文':90,'数学':88,'英语':75,'体育':80}
i=int(input('请输入成绩:'))

for i in grades:
    if i>=81:
        print(grades)

'''


'''
#对上面代码的改进:

grades = {'语文': 90, '数学': 88, '英语': 75, '体育': 80}

for subject, score in grades.items():   # 同时遍历键和值
    if score > 81:                      # 判断成绩是否大于81
        print(subject, score)           # 输出科目和成绩
'''




#老师的
grades={'语文':90,'数学':88,'英语':75,'体育':80}

for i in grades:
    if grades[i]>81:
        print(i,grades[i])
