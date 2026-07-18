from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '26236197'
API_KEY = 'NntwdHo4GZMIckCVsi3Io6LQ'
SECRET_KEY = 'Z5VaoLRbwyfGa1LZWVwwywf0AFmjKFGd'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
    
image=get_file_content('身份证.png')

idCardSide="back"

#调用身份证识别
res_image=client.idcard(image,idCardSide)
print(res_image)



'''
对上面代码的改进:

import os
import sys
from dotenv import load_dotenv
from aip import AipOcr

# 从 .env 文件读取密钥
load_dotenv()
APP_ID = os.environ.get('BAIDU_APP_ID')
API_KEY = os.environ.get('BAIDU_API_KEY')
SECRET_KEY = os.environ.get('BAIDU_SECRET_KEY')

if not all([APP_ID, API_KEY, SECRET_KEY]):
    sys.exit('请先设置环境变量或创建 .env 文件，包含 BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY')

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file_path):
    """读取文件二进制内容，若文件不存在则报错"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'文件不存在: {file_path}')
    with open(file_path, 'rb') as f:
        return f.read()


def recognize_idcard(image_path, side='front'):
    """
    识别身份证
    :param image_path: 图片路径
    :param side: 'front' 正面, 'back' 背面
    :return: 识别成功返回关键信息字典，失败返回 None
    """
    try:
        image = get_file_content(image_path)
    except FileNotFoundError as e:
        print(e)
        return None

    # 调用百度身份证识别接口
    result = client.idcard(image, id_card_side=side)

    # 判断是否识别出错
    if 'error_code' in result:
        print(f"识别失败，错误码：{result['error_code']}，原因：{result['error_msg']}")
        return None

    # 提取并展示关键信息
    words_result = result.get('words_result', {})
    if not words_result:
        print('未识别到身份证信息')
        return None

    print('======== 识别结果 ========')
    if side == 'front':
        info = {
            '姓名': words_result.get('姓名', {}).get('words', ''),
            '性别': words_result.get('性别', {}).get('words', ''),
            '民族': words_result.get('民族', {}).get('words', ''),
            '出生': words_result.get('出生', {}).get('words', ''),
            '住址': words_result.get('住址', {}).get('words', ''),
            '身份证号': words_result.get('公民身份号码', {}).get('words', ''),
        }
    else:
        info = {
            '签发机关': words_result.get('签发机关', {}).get('words', ''),
            '有效期限': words_result.get('有效期限', {}).get('words', ''),
        }

    for key, value in info.items():
        print(f'{key}: {value}')
    print('=========================')
    return info


if __name__ == '__main__':
    # 默认图片路径，你可以通过命令行参数传入，这里简单用变量
    img_file = '身份证.png'
    side = 'front'            # 或 'front'

    recognize_idcard(img_file, side)
    
    '''