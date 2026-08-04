#用random生成10个两位数,将其中的奇数和偶数分别存入两个列表中,然后将列表按降序排序并统计每个列表包含的元素个数

import random

list1=[]
list2=[]

for i in range(10):
    num=random.randint(10,99)
    if num%2==1:
        list1.append(num)
    else:
        list2.append(num)
    list1.sort()
    list2.sort(reverse=True)

print('奇数为:',list1,'共有:',len(list1),'个')
print('偶数为:',list2,'共有:',len(list2),'个')


'''
对上面代码的改进:

import random

odd_nums = []
even_nums = []

for _ in range(10):
    num = random.randint(10, 99)
    if num % 2 == 1:
        odd_nums.append(num)
    else:
        even_nums.append(num)

# 循环结束后统一降序排序
odd_nums.sort(reverse=True)
even_nums.sort(reverse=True)

print('奇数为:', odd_nums, '共有:', len(odd_nums), '个')
print('偶数为:', even_nums, '共有:', len(even_nums), '个')

'''