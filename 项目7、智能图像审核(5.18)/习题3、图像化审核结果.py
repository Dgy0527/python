from aip import AipImageCensor
from PIL import Image,ImageFont,ImageDraw

""" 你的 APPID AK SK """
APP_ID = '62511473'
API_KEY = 'Yt7BZ9RHTu88x1OxWPRJ1tjf'
SECRET_KEY = 'DKEEXm1iltlLMzod5BDhVf1RhASbwGet'

client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

"""调用色情识别接口"""
filename='images/luxun.jpg'
im1=Image.open(filename)
result=client.imageCensorUserDefined(get_file_content(filename))
print(result)

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
    ziti=ImageFont.truetype(r'C\Windows\Fonts\SIMYOU.TTF',10)
    quyu=ImageDraw.Draw(im1)
    quyu.text((0,0),msg,fill='red',font=ziti)
im1.show()
im1.save('new1.jpg')



'''
对上面代码的改进:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
图片内容审核工具
- 使用百度AI图像审核接口
- 密钥从 .env 文件读取
- 修复了API报错时静默退出的漏洞
"""

import os
import sys
import logging
from dotenv import load_dotenv
from aip import AipImageCensor
from PIL import Image, ImageFont, ImageDraw

# ---------- 配置日志 ----------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# ---------- 加载 .env 环境变量 ----------
load_dotenv()

APP_ID = os.getenv('BAIDU_APP_ID')
API_KEY = os.getenv('BAIDU_API_KEY')
SECRET_KEY = os.getenv('BAIDU_SECRET_KEY')

# 调试环境变量是否读取成功（读取后可以删掉或注释掉下面这一行）
# print(f"【调试】当前读取到的 APP_ID 是: {APP_ID}")

if not all([APP_ID, API_KEY, SECRET_KEY]):
    logging.error("环境变量缺失！请确保 .env 文件中包含 BAIDU_APP_ID、BAIDU_API_KEY、BAIDU_SECRET_KEY")
    sys.exit(1)

# ---------- 初始化百度AI客户端 ----------
client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file_path: str) -> bytes:
    """读取文件内容（二进制）"""
    try:
        with open(file_path, 'rb') as fp:
            return fp.read()
    except FileNotFoundError:
        logging.error(f"文件不存在: {file_path}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"读取文件失败: {e}")
        sys.exit(1)


def process_image(input_path: str, output_path: str) -> None:
    """
    处理单张图片：
    1. 调用百度审核接口
    2. 若接口报错，立刻打印错误并退出
    3. 若不合规或疑似，在图片底部绘制提示文字
    """
    try:
        # ---------- 1. 读取图片并调用审核接口 ----------
        image_data = get_file_content(input_path)
        result = client.imageCensorUserDefined(image_data)
        logging.info(f"审核结果: {result}")

        # ====================【重点修复】====================
        # 优先判断 API 是否返回错误码，防止后续解析报错且静默退出
        if 'error_code' in result:
            logging.error(f"百度 API 调用失败！错误码: {result['error_code']}, 错误信息: {result.get('error_msg', '未知错误')}")
            sys.exit(1)
        # ==================================================

        # ---------- 2. 解析审核结论 ----------
        conclusion = result.get('conclusion', '')
        if conclusion not in ('不合规', '疑似'):
            logging.info(f"审核结果为 '{conclusion}'，合规，无需标注。")
            return

        # 提取违规原因
        data_list = result.get('data', [])
        msg_parts = []
        for item in data_list:
            msg = item.get('msg', '')
            if msg:
                msg_parts.append(msg)
        msg_text = ','.join(msg_parts) if msg_parts else '疑似违规（无详细信息）'
        logging.info(f"违规提示: {msg_text}")

        # ---------- 3. 加载图片并准备绘制 ----------
        try:
            img = Image.open(input_path)
        except Exception as e:
            logging.error(f"无法打开图片 {input_path}: {e}")
            sys.exit(1)

        draw = ImageDraw.Draw(img)
        width, height = img.size

        # ---------- 4. 动态选择字体 ----------
        font_size = max(10, min(40, height // 20))
        try:
            # Windows 系统常用中文字体路径
            font_path = r'C:\Windows\Fonts\SimHei.ttf' # 黑体
            if not os.path.exists(font_path):
                font_path = r'C:\Windows\Fonts\msyh.ttc' # 微软雅黑
            if not os.path.exists(font_path):
                font = ImageFont.load_default()
                logging.warning("未找到常用中文字体，使用默认字体（可能无法显示中文）")
            else:
                font = ImageFont.truetype(font_path, font_size)
        except:
            font = ImageFont.load_default()
            logging.warning("加载字体异常，使用默认字体")

        # ---------- 5. 文字自动换行 ----------
        text_full = f"审核结果：{msg_text}"
        lines = []
        current_line = ''
        for ch in text_full:
            current_line += ch
            # 左右各留20像素边距,计算字符宽度是否超出
            if draw.textlength(current_line, font=font) > width - 40:
                lines.append(current_line[:-1])
                current_line = current_line[-1]
        if current_line:
            lines.append(current_line)

        # ---------- 6. 在图片底部居中绘制 ----------
        line_spacing = font_size + 6
        total_text_height = len(lines) * line_spacing
        y_start = height - total_text_height - 20

        for i, line in enumerate(lines):
            line_width = draw.textlength(line, font=font)
            x = (width - line_width) / 2
            y = y_start + i * line_spacing
            draw.text((x, y), line, fill='red', font=font)

        # ---------- 7. 保存图片并显示 ----------
        try:
            img.save(output_path)
            logging.info(f"处理完成，已保存至: {output_path}")
            img.show()
        except Exception as e:
            logging.error(f"保存图片失败: {e}")
            sys.exit(1)

    except Exception as e:
        logging.error(f"处理过程中发生未预期错误: {e}")
        sys.exit(1)


# ---------- 主程序入口 ----------
if __name__ == '__main__':
    # 建议改成绝对路径防止找不到文件，例如：
    # INPUT_IMAGE = r'D:\Git\项目7、智能图像审核(5.18)\images\luxun.jpg'
    INPUT_IMAGE = 'images/luxun.jpg'
    OUTPUT_IMAGE = 'new1.jpg'

    if not os.path.exists(INPUT_IMAGE):
        logging.error(f"输入图片不存在: {INPUT_IMAGE}")
        sys.exit(1)

    process_image(INPUT_IMAGE, OUTPUT_IMAGE)

'''