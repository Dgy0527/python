#复制并统计图片文件
import os
import shutil #shutil库:是高级的文件、文件夹、压缩包处理模块

dir_files=(os.listdir(os.getcwd())) #以列表的形式返回当前文件夹中的所有文件
print('当前文件夹下共有',len(dir_files),'个文件(夹)',dir_files)

new_dir=input('请输入你要新建的文件夹名字:')
os.mkdir(new_dir)

cn=0
print('\n图片文件开始复制:')
for file in dir_files:
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif') or file.endswith('.webp'):
        cn+1
        shutil.copyfile(file,new_dir+'/'+file)
        print(file,'已复制')
print('共复制了',cn,'个图片文件')
print(new_dir,'文件夹中的文件:',os.listdir(new_dir))


'''
import os
import shutil

current_dir = os.getcwd()
all_items = os.listdir(current_dir)
print('当前文件夹共有', len(all_items), '个项目:', all_items)

new_dir = input('请输入新建文件夹名称: ')
new_dir_path = os.path.join(current_dir, new_dir)

if not os.path.exists(new_dir_path):
    os.mkdir(new_dir_path)
else:
    print('文件夹已存在，将使用现有文件夹')

image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.JPEG', '.PNG', '.GIF', '.WEBP')
copied_count = 0

print('\n开始复制图片文件:')
for item in all_items:
    src_path = os.path.join(current_dir, item)
    if os.path.isfile(src_path) and item.lower().endswith(image_extensions):
        try:
            shutil.copyfile(src_path, os.path.join(new_dir_path, item))
            copied_count += 1
            print(item, '已复制')
        except Exception as e:
            print('复制失败', item, ':', e)

print('共复制了', copied_count, '个图片文件')
print(new_dir, '文件夹中的文件:', os.listdir(new_dir_path))
'''