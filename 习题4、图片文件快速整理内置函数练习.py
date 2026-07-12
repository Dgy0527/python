#内置函数练习
'''
1、len()函数:返回对象的长度和元素的个数
2、str()函数:返回该对象转换成字符串数据类型
3、转文符:\n 换行,\退格,\t 水平制表,\续行符
4、endswitch()函数:用于判断字符串是否以指定后缀结尾,是否返回True,否则返回Flase
'''

a='python'
print(len(a))

color=['red','green','blue']
print(len(color))

print('\n')

x='深圳'
y=2026
print(x+str(y))

print('python'.endswith('py'))
print('python'.endswith('on'))
print('22.txt'.endswith('.txt'))

x='333.doc'
print(x.endswith('doc'))