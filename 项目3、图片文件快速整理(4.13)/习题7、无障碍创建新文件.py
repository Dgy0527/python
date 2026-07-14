#无障碍创建文件夹

import os
import shutil #shutil库:是高级的文件、文件夹、压缩包处理模块

dir_files=(os.listdir(os.getcwd())) #以列表的形式返回当前文件夹中的所有文件
print('当前文件夹下共有',len(dir_files),'个文件(夹)',dir_files)

while True:
    new_dir=input('请输入你要新建的文件夹名字:')
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print('文件夹',new_dir,'已新建,等待图片复制。')
        break
    else:
        print('文件夹',new_dir,'已存在,请再输入一个文件夹名字:')

cn=0
print('\n图片文件开始复制:')

for file in dir_files:
    if file.endswith('456.jpg') or file.endswith('.png') or file.endswith('.gif') or file.endswith('.webp'):
        if file.endswith('456.jpg'):
            file_ext='456.jpg'
        elif file.endswith('.png'):
            file_ext='.png'
        elif file.endswith('.gif'):
            file_ext='.gif'
        else:
            file_ext='.webp'
        cn+=1
        new_file=str(cn)+file_ext
        shutil.copyfile(file,new_dir+'/'+new_file)
        print(file,'已复制')
print('共复制了',cn,'个图片文件')
print(new_dir,'文件夹中的文件:',os.listdir(new_dir))


'''
对上面代码的改进:

import shutil
from pathlib import Path
import re

def main():
    # 1. 当前目录与文件获取（使用 pathlib 跨平台，不怕斜杠问题）
    current_dir = Path.cwd()
    files = [f for f in current_dir.iterdir() if f.is_file()]
    print(f"当前文件夹下共有 {len(files)} 个文件。")

    # 2. 输入校验（防非法字符，注意外层已改为单引号，避免和里面的双引号冲突）
    while True:
        new_dir = input("请输入你要新建的文件夹名字：").strip()
        if not new_dir:
            print("文件夹名不能为空，请重新输入。")
            continue
        if re.search(r'[\\/:*?"<>|]', new_dir):
            print('文件夹名包含非法字符（如 / : * ? " < > |），请重新输入。')
            continue
        
        target_path = current_dir / new_dir
        try:
            target_path.mkdir(exist_ok=False)
            print(f"文件夹 {new_dir} 创建成功！")
            break
        except FileExistsError:
            print(f"文件夹 {new_dir} 已存在，请换一个名字。")
        except Exception as e:
            print(f"创建失败：{e}")

    # 3. 图片筛选与排序（按修改时间倒序，最新的放前面）
    exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')
    img_files = [f for f in files if f.suffix.lower() in exts]
    img_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    total = len(img_files)

    # 4. 复制（带单行刷新进度，不刷屏）
    print(f"\n共发现 {total} 张图片，开始复制...")
    for idx, f in enumerate(img_files, start=1):
        new_name = f"{idx}{f.suffix}"
        dst = target_path / new_name
        try:
            shutil.copyfile(f, dst)
            print(f"\r进度: {idx}/{total} -> {new_name} 已复制", end="")
        except Exception as e:
            print(f"\n复制 {f.name} 失败：{e}")
    
    print("\n\n复制完成!")
    
    # 5. 展示结果
    if total > 0:
        print(f"{new_dir} 文件夹中的文件：")
        for item in target_path.iterdir():
            print(f"  {item.name}")

if __name__ == "__main__":
    main()

'''