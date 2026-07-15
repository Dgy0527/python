
#知识点练习
#1、random库:用于生成伪随机数
import random #导入库
a=random.randint(0,10) #产生一个0-10之间的整数
print(a)

#2、列表:是数据类型,也是序列,用一对中括号定义,列表中的每个元素用逗号分隔,双向检索或逆向检索
list1=['red','blue','深圳职业技术大学','深圳大学',2026,600] #定义一个一维列表
print(list1)
print(list1[0])
print(list1[-2])
print(list1[2:5])
print(len(list1))

for i in list1:
    print(i)

#3、列表相关函数和方法的练习
list2=[3,8,6,5,7,2,9]
print(list2)

list2.append(20) #1、在列表末尾添加一个元素
print(list2)

list2.sort() #2、对列表进行升序排序
print(list2)

list2.sort(reverse=True) #3、对列表进行降序排序
print(list2)

del list2[-1] #4、删除最后一个元素
print(list2)

list2.insert(3,18) #5、表示在下表为3的位置插入一个元素18
print(list2)

#6、二维列表:在二维列表中再嵌套一个列表,中括号中还有中括号
list3=[['s01',8,6,4,7],['s02',7,8,9,4],['s03',6,4,8,9],['s04',4,8,5,3]] #定义一个二维列表
print(list3)

list3_sort=sorted(list3,key=lambda e:e[4],reverse=True) #对二维列表进行降序排序
print(list3_sort)

for i in list3_sort:
    print(i)

#7、字典:是数据类型,大括号定义,每个元素由键值对组成,键名:键值，元素之间用逗号分隔,字典是无序可变的序列
dic1={'s01':3.1,'s02':2.5,'s03':3.1,'s04':3.1,'s05':3.1,'s06':3.1,'s07':3.1,'s08':3.1} #定义字典
print(dic1)
print(dic1['s01']) #输出字典中某个元素的值
print(dic1.get('s01')) #输出字典中的某个元素的值

dic1['s09']=3.4
print(dic1)

del dic1['s09']
print(dic1)

#6、一键对多值的字典
dic2={
    's01':['马丁','意大利',3.1],
    's02':['马丁','西班牙',2.8],
    's03':['理查德','挪威',2.5],
    's04':['马丁','意大利',3.1],
    's05':['马丁','意大利',3.1],
    's06':['马丁','意大利',3.1],
    's07':['马丁','意大利',3.1],
    's08':['马丁','意大利',3.1],   
}
print(dic2)
print(dic2['s01'][2])



'''
对上面代码的改进:

import random

# 1. random库:用于生成伪随机数
# 【修正】randint 不接受关键字参数 a=0, b=10,直接写 (0, 10)
a = random.randint(0, 10)  
print("随机数 a =", a)

print("-" * 30)

# 2. 列表：定义和基本操作
list1 = ['red', 'blue', '深圳职业技术大学', '深圳大学', 2026, 600]
print("list1 =", list1)
print("list1[0] =", list1[0])
print("list1[-2] =", list1[-2])      # 倒数第二个元素
print("list1[2:5] =", list1[2:5])    # 切片
print("len(list1) =", len(list1))

print("--- 遍历 list1 ---")
for i in list1:
    print(i)

print("-" * 30)

# 3. 列表相关函数和方法
list2 = [3, 8, 6, 5, 7, 2, 9]
print("原始 list2 =", list2)

list2.append(20)                     # 末尾添加元素
print("append(20) 后 =", list2)

list2.sort()                         # 升序排序
print("升序排序后 =", list2)

list2.sort(reverse=True)             # 降序排序
print("降序排序后 =", list2)

list2.pop()                          # 删除最后一个元素（比 del list2[-1] 更常用，也可获取被删的值）
print("pop() 删除末尾后 =", list2)

list2.insert(3, 18)                  # 在下标为3的位置插入18
print("insert(3, 18) 后 =", list2)

print("-" * 30)

# 4. 二维列表
# 【修正】注释改为“定义一个二维列表”
list3 = [['s01', 8, 6, 4, 7], 
         ['s02', 7, 8, 9, 4], 
         ['s03', 6, 4, 8, 9], 
         ['s04', 4, 8, 5, 3]]
print("原始 list3 =", list3)

# 按每行第5列(索引4)降序排序
list3_sort = sorted(list3, key=lambda e: e[4], reverse=True)
print("按第5列降序排序后的 list3_sort =")
for row in list3_sort:
    print(row)

print("-" * 30)

# 5. 字典
dic1 = {'s01': 3.1, 's02': 2.5, 's03': 3.1, 's04': 3.1, 's05': 3.1, 
        's06': 3.1, 's07': 3.1, 's08': 3.1}
print("原始 dic1 =", dic1)
print("dic1['s01'] =", dic1['s01'])
print("dic1.get('s01') =", dic1.get('s01'))

dic1['s09'] = 3.4                    # 添加新键值对
print("添加 s09 后 =", dic1)

del dic1['s09']                      # 删除键值对
print("删除 s09 后 =", dic1)

print("-" * 30)

# 6. 一键对多值的字典
dic2 = {
    's01': ['马丁', '意大利', 3.1],
    's02': ['马丁', '西班牙', 2.8],
    's03': ['理查德', '挪威', 2.5],
    's04': ['马丁', '意大利', 3.1],
    's05': ['马丁', '意大利', 3.1],
    's06': ['马丁', '意大利', 3.1],
    's07': ['马丁', '意大利', 3.1],
    's08': ['马丁', '意大利', 3.1],
}
print("dic2 =", dic2)
print("dic2['s01'][2] =", dic2['s01'][2])  # 输出 3.1

'''