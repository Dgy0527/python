#查询当前文件夹中的文本文件
#1、os库：提供了通用的、基本的操作系统交互功能
import os #导入库函数

print(os.getcwd()) #1、获取当前工作的文件夹
os.mkdir('new1') #2、创建一个新的文件夹
print(os.listdir('new1')) #3、以列表的形式返回指定文件夹中的所有文件
print(os.listdir(os.getcwd())) #以列表的形式返回当前文件夹中的所有文件
print(os.path.isfile('111.txt')) #4、path子库:isfile是判断指定的对象是否为文件,如果是返回True，否则返回Flase
print(os.path.isfile('new1')) 
print(os.path.isdir('111.txt')) #5、path子库：isdir是判断指定的对象是否为文件夹,如果是返回True,否则返回Flase
print(os.path.isdir('new1'))
print(os.path.exists('111.txt')) #6、path子库:exists是判断指定的对象是否存在,如果存在返回True，否则返回Flase
print(os.path.exists('1111.txt'))

dir_files=(os.listdir(os.getcwd())) #以列表的形式返回当前文件夹中的所有文件
print('当前文件夹下共有',len(dir_files),'个文件(夹)',dir_files)

print('\n文本文件包括如下:')
for file in dir_files:
    if file.endswith('.txt'):
        print(file)

'''
上面代码存在的问题:1、当new1这个文件存在时会报错
对上面代码的改进:
import os

print(os.getcwd()) # 1. 获取当前工作的文件夹

# 2. 创建一个新的文件夹(加判断避免重复创建报错)
if not os.path.exists('new1'):
    os.mkdir('new1')

print(os.listdir('new1')) # 3. 以列表的形式返回指定文件夹中的所有文件
print(os.listdir(os.getcwd())) # 以列表的形式返回当前文件夹中的所有文件

# 4. path子库: isfile是判断指定的对象是否为文件, 如果是返回True, 否则返回False(修正了原注释的"文件夹"错误)
print(os.path.isfile('111.txt')) 
print(os.path.isfile('new1')) 

# 5. path子库: isdir是判断指定的对象是否为文件夹, 如果是返回True, 否则返回False
print(os.path.isdir('111.txt')) 
print(os.path.isdir('new1'))

# 6. path子库: exists是判断指定的对象是否存在, 如果存在返回True, 否则返回False
print(os.path.exists('111.txt')) 
print(os.path.exists('1111.txt'))

dir_files = os.listdir(os.getcwd()) # 以列表的形式返回当前文件夹中的所有文件
print('当前文件夹下共有', len(dir_files), '个文件(夹)', dir_files)

print('\n文本文件包括如下:')
for file in dir_files:
    full_path = os.path.join(os.getcwd(), file)  # 拼接完整路径, 防止误判同名文件夹
    # 同时满足三个条件: 是文件, 后缀是.txt(不区分大小写)
    if os.path.isfile(full_path) and file.lower().endswith('.txt'):
        print(file)
'''