'''
1、内置函数:
    1)print:输出函数
    2)input:输入函数,输入的数据是字符串型
    3)int():转换函数,把字符串类型转换成整型
2、布尔型:True和Flase
3、比较运算符:==、！、=\>\<
4、逻辑运算符:and并、or或者、not非
5、选择结构(分支结构、条件结构、if结构)
    1)单分支:if
    2)双分支:if else
    3)多分支:if elif(多个) else 
'''

num=int(input('请输入一个整数:'))
#print(num+2)
if num>0:
    print('你输入的这个数',num,'是整数')
elif num<0:
    print('你输入的这个数',num,'是负数')
else:
    print('你输入的这个数',num,'是零')

if num%2==0:
    print('你输入的这个数',num,'是偶数')
else:
    print('你输入的这个数',num,'是奇数')