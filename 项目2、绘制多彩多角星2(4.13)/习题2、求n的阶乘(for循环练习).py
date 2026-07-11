#请输入一个整数n，计算其阶乘
'''
1、循环结构"表示程序重复执行某些动作,直到满足某条件时才可终止循环
2、for循环:遍历循环,就是从某个序列中的第一个元素到最后一个元素依次逐个访问
   循环执行的次数是根据遍历序列中元素的个数laiquedingde
3、语法规则:for 元素(循环变量) in 序列:循环体(代码块)
4、内置循环:print()输出;input()输入;int()转换函数:range()
5、range()函数:可创建一个整数序列;格式:range(start,stop,step)
'''

for i in range(5):
    print(i)
for i in range(1,11,2):
    print(i)
color=['red','green','yellow']
for j in color:
    print(j)
for a in [2,6,8]:
    print(a)

n=int(input('请输入一个整数'))
cn=1
for i in range(1,n+1):
    cn*=i #cn=cn*i
print('你输入的整数的阶乘为:',cn)
