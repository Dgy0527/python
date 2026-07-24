from aip import AipImageCensor
from PIL import Image,ImageFont,ImageDraw

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
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
        msg=msg+i['msg']+'\n'
        print('不合规的理由:',msg)


'''
对上面代码的改进:

import os
import sys
import logging
from dotenv import load_dotenv
from aip import AipImageCensor

# 加载 .env 文件
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_file_content(file_path):
    try:
        with open(file_path, 'rb') as fp:
            return fp.read()
    except FileNotFoundError:
        logging.error(f"文件不存在: {file_path}")
        sys.exit(1)
    except PermissionError:
        logging.error(f"没有权限读取文件: {file_path}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"读取文件失败: {e}")
        sys.exit(1)

def main():
    APP_ID = os.environ.get('BAIDU_APP_ID')
    API_KEY = os.environ.get('BAIDU_API_KEY')
    SECRET_KEY = os.environ.get('BAIDU_SECRET_KEY')

    if not all([APP_ID, API_KEY, SECRET_KEY]):
        logging.error("请设置环境变量 BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY(请检查 .env 文件是否存在且内容正确）")
        sys.exit(1)

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("请输入图片路径: ").strip()

    if not os.path.exists(filename):
        logging.error(f"文件不存在: {filename}")
        sys.exit(1)

    client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)

    try:
        result = client.imageCensorUserDefined(get_file_content(filename))
    except Exception as e:
        logging.error(f"API 调用失败: {e}")
        sys.exit(1)

    if 'error_code' in result:
        logging.error(f"API 返回错误: error_code={result['error_code']}, error_msg={result.get('error_msg')}")
        sys.exit(1)

    conclusion = result.get('conclusion', '未知')
    logging.info(f"审核结论: {conclusion}")

    if conclusion in ('不合规', '疑似'):
        data = result.get('data', [])
        if not data:
            logging.warning("结论为不合规或疑似，但未返回详细违规信息")
        else:
            reasons = []
            for item in data:
                if 'msg' in item:
                    reasons.append(item['msg'])
            if reasons:
                logging.info("违规理由:\n" + "\n".join(reasons))
            else:
                logging.info("未获取到具体违规理由")
    else:
        logging.info("图片合规")

if __name__ == '__main__':
    main()
'''