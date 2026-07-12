#查询当前文件夹中的文本文件
import os #os库:提供了通用的、基本的操作系统文件功能

print(os.getcwd()) #获取当前工作的文件夹
os.mkdir('D:/Git/new1(项目2)') #创建一个新的文件夹


print(os.listdir('new1(项目2)')) #以列表的形式返回指定文件夹下的所有内容
print(os.listdir(os.getcwd()))
print(os.path.isfile('new1')) #返回指定对象是否为文件
print(os.path.isfile('555.txt')) #返回指定对象是否为文件夹
print(os.path.isdir('new1(项目2)')) #返回指定对象是否为文件夹
print(os.path.exists('555.txt')) #返回指定对象是否存在，存在则True，否则False
print(os.path.exists('55.txt')) #返回指定对象是否存在，存在则True，否则False

dir_file=os.listdir(os.getcwd())
print('当前文件夹下共有',len(dir_file),'个文件夹或文件',dir_file)
print('\n文本文件包括:')
for file in dir_file:
    if file.endswith('.txt'):
        print(file)


'''
上面的代码存在的问题:1、不能在项目2这个目录里面运行;
                   2、当new1这个文件存在时运行会报错
对上面代码的改进:

# 查询当前文件夹中的文本文件
import os

# 1. 精确获取当前代码文件所在的目录（即 项目2 那个文件夹）
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将当前工作目录切换到脚本所在的目录，这样后面的相对路径写法就都能对上
os.chdir(current_dir)

print("当前工作目录:", os.getcwd())


# 2. 创建文件夹 new1(项目2)
folder_name = 'new1(项目2)'
os.makedirs(folder_name, exist_ok=True) # exist_ok=True 保证如果文件夹已存在，不会报错
print("已确认文件夹:", folder_name)


# 3. 生成几个用来测试的文本文件
# 在当前目录下生成 555.txt 和 55.txt
for file_name in ['555.txt', '55.txt']:
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("这是一个测试文本文件。")

# 在 new1(项目2) 文件夹内生成 666.txt 和 777.txt
for file_name in ['666.txt', '777.txt']:
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("这是一个测试文本文件。")

print("已生成测试用的 .txt 文件。\n")


# 4. 目录查询和属性判断
print("new1(项目2) 目录下的内容:", os.listdir(folder_name))
print("当前目录下的所有内容:", os.listdir(os.getcwd()))

print("'new1(项目2)' 是文件吗?", os.path.isfile(folder_name))      # False，因为它是文件夹
print("'555.txt' 是文件吗?", os.path.isfile('555.txt'))            # True，文件已生成
print("'new1(项目2)' 是文件夹吗?", os.path.isdir(folder_name))     # True
print("'555.txt' 存在吗?", os.path.exists('555.txt'))              # True
print("'55.txt' 存在吗?", os.path.exists('55.txt'))                # True


# 5. 查找当前目录及子文件夹内所有的 .txt 文件
print("\n查找到的文本文件包括:")
found_file_count = 0
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.txt'):
            print(os.path.join(root, file))
            found_file_count += 1

if found_file_count == 0:
    print("当前目录下没有找到任何 .txt 文件。")
'''
