#快速复制JPG文件
import os
import shutil #shutil库:是高级的文件、文件夹、压缩包处理模块

dir_files=(os.listdir(os.getcwd())) #以列表的形式返回当前文件夹中的所有文件
print('当前文件夹下共有',len(dir_files),'个文件(夹)',dir_files)

new_dir=input('请输入你要新建的文件夹名字:')
os.mkdir(new_dir)

print('\n图片文件开始复制:')
for file in dir_files:
    if file.endswith('填入你要复制的图片的.jpg'):
        shutil.copyfile(file,new_dir+'/'+file)
        print(file,'已复制')

print(new_dir,'文件夹中的文件:',os.listdir(new_dir))