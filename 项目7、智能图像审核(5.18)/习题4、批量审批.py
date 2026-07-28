from aip import AipImageCensor
from PIL import Image,ImageFont,ImageDraw
import os,time

""" 你的 APPID AK SK """
APP_ID = '625537873'
API_KEY = 'Yt7BZ9RpGu88x1ogWPRJ1tjf'
SECRET_KEY = 'DKEEXm1iltlLbgzod5BDhVf1RhASbwGet'
client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath): #1个用法
    with open(filePath,'rb') as fp:
        return fp.read()

"""调用色情识别接口"""
file=os.listdir('images')
for i in file:
    filename='images/'+i
    #im1=Image.open(filename)
    result=client.imageCensorUserDefined(get_file_content(filename))
    #print(result)

    #JSON格式解析
    jielun=result['conclusion']
    print('解析结果:',jielun)

    if jielun=='不合规' or jielun=='疑似':
        jielunlist=result['data']
        msg=''

        for i in jielunlist:
            msg=msg+i['msg']
        print('不合规的理由:',msg)

        #图像化审核开始
        im1=Image.open(filename)
        im2=Image.open('wrong.jpg')
        ziti=ImageFont.truetype(r'C:\Windows\Fonts\SIMYOU.TTF',10)
        im1.paste(im2,(0,0))
        quyu=ImageDraw.Draw(im1)
        quyu.text((0,0),msg,fill='red',font=ziti)
    im1.show()
time.sleep(1)


'''
对上面代码的改进:

from aip import AipImageCensor
from PIL import Image, ImageFont, ImageDraw
import os
import time

APP_ID = '6255338873'
API_KEY = 'Yt7BZ9RpGu8845OxWPRJ1tjf'
SECRET_KEY = 'DKEEXm1iltlLlzod5BDhVf1RhAolwGet'

# 核心修改：将 client 作为参数传入 process_image 函数
def process_image(client, image_path, output_dir='output', wrong_img_path='wrong.jpg', font_path=r'C:\Windows\Fonts\SIMYOU.TTF'):
    """处理单张图片：审核 -> 标记 -> 自动保存"""
    try:
        # 1. 调用审核接口
        with open(image_path, 'rb') as f:
            result = client.imageCensorUserDefined(f.read())
        
        conclusion = result.get('conclusion', '')
        
        # 2. 只有不合规或疑似才进行标记和保存
        if conclusion in ('不合规', '疑似'):
            data = result.get('data', [])
            msg = ';'.join([item.get('msg', '') for item in data if 'msg' in item])
            print(f' {os.path.basename(image_path)} 审核未通过：{msg}')
            
            # 标记图片
            im1 = Image.open(image_path)
            im2 = Image.open(wrong_img_path)
            im2 = im2.resize(im1.size, Image.LANCZOS)  # 缩放到原图大小覆盖全图
            im1.paste(im2, (0, 0))
            
            draw = ImageDraw.Draw(im1)
            try:
                font = ImageFont.truetype(font_path, 20)
            except:
                font = ImageFont.load_default()
            # 文字放底部居中
            bbox = draw.textbbox((0, 0), msg, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
            x = (im1.width - text_w) // 2
            y = im1.height - text_h - 10
            draw.text((x, y), msg, fill='red', font=font)
            
            # 自动保存到输出文件夹
            os.makedirs(output_dir, exist_ok=True)
            save_path = os.path.join(output_dir, os.path.basename(image_path))
            im1.save(save_path)
            print(f' 已保存标记图片：{save_path}')
            
        else:
            print(f' {os.path.basename(image_path)} 审核通过（{conclusion}），无需标记')
            
    except Exception as e:
        print(f' 处理 {image_path} 出错：{e}')

def main():
    # 在这里初始化 client
    client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)
    
    images_dir = 'images'
    if not os.path.isdir(images_dir):
        print(f'目录 {images_dir} 不存在')
        return
    
    valid_ext = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    files = [f for f in os.listdir(images_dir) if f.lower().endswith(valid_ext)]
    
    print(f'共找到 {len(files)} 张图片，开始全自动审核...')
    for idx, filename in enumerate(files):
        file_path = os.path.join(images_dir, filename)
        print(f'\n处理第 {idx+1}/{len(files)} 张：{filename}')
        
        # 核心修改：调用时把 client 传进去
        process_image(client, file_path)
        
        time.sleep(1.5)  # 每张间隔1.5秒,避免API限流

if __name__ == '__main__':
    main()
'''