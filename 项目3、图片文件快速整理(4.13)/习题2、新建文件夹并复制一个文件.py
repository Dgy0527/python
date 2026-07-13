#先新建一个文件夹并复制一个文件到此文件夹中
import os
import shutil #shutil库:是高级的文件、文件夹、压缩包处理模块
#shutil.copyfile('111.txt','D:/222222.txt') #将源文件复制为目标文件
dir_files=(os.listdir(os.getcwd())) #以列表的形式返回当前文件夹中的所有文件
print('当前文件夹下共有',len(dir_files),'个文件(夹)',dir_files)

new_dir=input('请输入你要新建的文件夹名字:')
os.mkdir(new_dir)

file=input('请输入你要复制的文件名字:')
shutil.copyfile(file,new_dir+'/'+file)
print(file,'已复制完成。')

print(new_dir,'文件夹中的文件:',os.listdir(new_dir))

print('\n文本文件包括如下:')
for file in dir_files:
    if file.endswith('.txt'):
        print(file)


'''
上面代码存在的问题:1、没有判断文件夹是否已存在
改进如下:
import os
import shutil

# 1. 获取当前目录文件列表
dir_files = os.listdir(os.getcwd())
print('当前文件夹下共有', len(dir_files), '个文件(夹)', dir_files)

# 2. 新建文件夹（加防重复判断）
new_dir = input('请输入你要新建的文件夹名字:')
if os.path.exists(new_dir):
    print(f'警告：文件夹 "{new_dir}" 已存在，将直接使用该文件夹。')
else:
    os.mkdir(new_dir)
    print(f'文件夹 "{new_dir}" 创建成功。')

# 3. 复制文件（加源文件存在性判断，并兼容路径）
file = input('请输入你要复制的文件名字（如需带路径请完整输入）:')
if not os.path.exists(file):
    print(f'错误：文件 "{file}" 不存在，复制失败。')
else:
    # 生成目标路径（跨平台）
    dest_path = os.path.join(new_dir, file)
    
    # 确保目标文件夹的父目录存在（处理带路径的情况）
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)  # 自动创建缺失的父目录
    
    shutil.copyfile(file, dest_path)
    print(f'"{file}" 已成功复制到 "{dest_path}"。')

# 4. 查看新建文件夹里的内容
print(f'\n"{new_dir}" 文件夹中的文件:', os.listdir(new_dir))

# 5. 查看新建文件夹里的 txt 文件（修正为查看新目录）
print(f'\n"{new_dir}" 文件夹中的文本文件如下:')
new_files = os.listdir(new_dir)
for f in new_files:
    if f.endswith('.txt'):
        print(f)
'''