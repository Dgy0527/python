#导入PIL中的Image模块，先打开图片source.jpg,再根据图片的尺寸,设置好裁剪区域左上角和右下角的大致坐标范围,可以将其保存到一个元组或列表中。
#使用图像的crop方法,按设定的坐标区域裁剪,得到一个新的图像,最后将图像保存为文件target.jpg

from PIL import Image

image=Image.open('source.jpg')
region=(150,225,350,450)
img_cut=image.crop(region)
img_cut.show()
img_cut.save('target.jpg')


'''
对上面代码的改进:

from PIL import Image
import os

def crop_image(source_path, target_path, crop_region):
    """
    裁剪图片并保存
    :param source_path: 原图片路径
    :param target_path: 保存裁剪后图片的路径
    :param crop_region: 裁剪区域元组 (左, 上, 右, 下)
    """
    # 1. 检查文件是否存在
    if not os.path.exists(source_path):
        print(f"错误：找不到文件 {source_path}")
        return

    try:
        # 2. 打开图片
        image = Image.open(source_path)
        
        # 3. 打印图片尺寸，方便后续调试坐标
        print(f"图片尺寸: {image.size}") 

        # 4. 执行裁剪 (裁剪区域：左, 上, 右, 下)
        img_cut = image.crop(crop_region)

        # 5. 预览并保存
        # img_cut.show() # 如果需要弹出窗口预览，取消注释这行
        img_cut.save(target_path)
        print(f"成功！裁剪后的图片已保存至：{target_path}")

    except Exception as e:
        print(f"裁剪过程中发生错误：{e}")

# ============ 使用示例 ============
# 裁剪原图第二行中间的男性头像
region = (160, 225, 340, 435)  # (左, 上, 右, 下)

crop_image('source.jpg', 'target.jpg', region)

'''