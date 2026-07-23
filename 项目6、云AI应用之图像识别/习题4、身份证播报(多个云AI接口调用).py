from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '26236197'
API_KEY = 'NntwdHo4GZMIckCVsi3Io6LQ'
SECRET_KEY = 'Z5VaoLRbwyfGa1LZWVwwywf0AFmjKFGd'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath): #一个用法
    with open(filePath,'rb') as fp:
        return fp.read()

image=get_file_content('身份证.png')

idCardSide='back'

#调用身份证识别
res_image=client.idcard(image,idCardSide)
print(res_image)

#JSON解析
result={'idcard_number_type': 1, 'words_result': {'姓名': {'location': {'top': 41, 'left': 73, 'width': 45, 'height': 20}, 'words': '徐乐'},
        '民族': {'location': {'top': 75, 'left': 148, 'width': 17, 'height': 18}, 'words': '汉'},
        '住址': {'location': {'top': 137, 'left': 70, 'width': 164, 'height': 38},
         'words': '安徽省宿州市埇桥区朱仙庄镇'}, '公民身份号码': {'location': {'top': 217, 'left': 132, 'width': 215, 'height': 18},
        'words': '652901196611026716'}, '出生': {'location': {'top': 105, 'left': 71, 'width': 128, 'height': 18},
        'words': '19661102'}, '性别': {'location': {'top': 75, 'left': 70, 'width': 14, 'height': 18}, 'words': '男'}},
        'words_result_num': 6, 'image_status': 'reversed_side', 'log_id': 2053653013504731044}
print('姓名：',result['words_result']['姓名']['words'])
print('性别：',result['words_result']['性别']['words'])
sfzhm=result['words_result']['公民身份号码']['words']

year=sfzhm[6:10]
month=sfzhm[10:12]
day=sfzhm[12::14]
print('生日:',year+'年'+month+'月'+day+'日')
print('住址：',result['words_result']['住址']['words'])

#语音播报开始
text='''
姓名:徐乐
性别:男
生日:1966年11月02日
住址:安徽省宿州市埇桥区朱仙镇
'''

from aip import AipSpeech
import os

""" 你的 APPID AK SK """
APP_ID = '11437531'
API_KEY = 'UX8G6WKs0qAtlhgBC1nLylsq'
SECRET_KEY = 'pntVHwrfcwASqEQOAYBD23LcCAv9oGaT'

client1 = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result=client1.synthesis(text,'zh',1,{
    'vol':5,
})

#识别正确返回语音二进制,错误则返回dict，参照下面错误码
if not isinstance(result,dict):
    with open('身份证播报.mp3','wb') as f:
        f.write(result)
os.system('身份证播报.mp3')


'''
上面代码存在的问题:1、idCardSide = 'back' 原本是应该识别正面的,'front'

对上面代码的改进:
import os
import sys
from dotenv import load_dotenv
from aip import AipOcr, AipSpeech

# 强制使用绝对路径读取同目录下的 .env
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')
load_dotenv(env_path)

# 从环境变量中读取密钥
APP_ID_OCR = os.environ.get('BAIDU_OCR_APP_ID')
API_KEY_OCR = os.environ.get('BAIDU_OCR_API_KEY')
SECRET_KEY_OCR = os.environ.get('BAIDU_OCR_SECRET_KEY')

APP_ID_TTS = os.environ.get('BAIDU_TTS_APP_ID')
API_KEY_TTS = os.environ.get('BAIDU_TTS_API_KEY')
SECRET_KEY_TTS = os.environ.get('BAIDU_TTS_SECRET_KEY')

# 打印一下，看看读到了什么（如果读到了数字，说明成功）
print(f"【调试】读取到 OCR APP_ID: {APP_ID_OCR}")
print(f"【调试】读取到 TTS APP_ID: {APP_ID_TTS}")

# 如果读不到，直接提示错误
if not all([APP_ID_OCR, API_KEY_OCR, SECRET_KEY_OCR, APP_ID_TTS, API_KEY_TTS, SECRET_KEY_TTS]):
    raise ValueError("环境变量读取失败！请检查 .env 文件是否在代码同目录下，且内容已完全替换！")

# 初始化客户端
ocr_client = AipOcr(APP_ID_OCR, API_KEY_OCR, SECRET_KEY_OCR)
tts_client = AipSpeech(APP_ID_TTS, API_KEY_TTS, SECRET_KEY_TTS)

def get_file_content(file_path):
    file_path = os.path.join(current_dir, file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"图片文件不存在: {file_path}")
    with open(file_path, 'rb') as fp:
        return fp.read()

def recognize_idcard(image_path, side='front'):
    image_data = get_file_content(image_path)
    result = ocr_client.idcard(image_data, side)
    if 'error_code' in result:
        raise Exception(f"OCR调用失败: {result.get('error_msg')}")
    return result

def extract_info(ocr_result):
    words_result = ocr_result.get('words_result', {})
    info = {
        '姓名': words_result.get('姓名', {}).get('words', ''),
        '性别': words_result.get('性别', {}).get('words', ''),
        '住址': words_result.get('住址', {}).get('words', ''),
        '身份证号': words_result.get('公民身份号码', {}).get('words', '')
    }
    id_num = info['身份证号']
    if len(id_num) == 18:
        year = id_num[6:10]
        month = id_num[10:12]
        day = id_num[12:14]
        info['生日'] = f"{year}年{month}月{day}日"
    else:
        info['生日'] = '解析失败'
    return info

def synthesize_speech(text, output_file='身份证播报.mp3'):
    result = tts_client.synthesis(text, 'zh', 1, {
        'vol': 5, 'spd': 5, 'pit': 5, 'per': 0
    })
    if not isinstance(result, dict):
        output_file = os.path.join(current_dir, output_file)
        with open(output_file, 'wb') as f:
            f.write(result)
        return output_file
    else:
        raise Exception(f"语音合成失败: {result.get('err_msg', '未知错误')}")

def play_audio(file_path):
    try:
        os.startfile(file_path) # Windows 系统播放
    except Exception as e:
        print(f"播放失败: {e}")

def main():
    image_path = '身份证.png'
    try:
        ocr_result = recognize_idcard(image_path, side='front')
        info = extract_info(ocr_result)

        for key, value in info.items():
            print(f"{key}: {value}")

        speech_text = f"姓名：{info['姓名']}，性别：{info['性别']}，生日：{info['生日']}，住址：{info['住址']}"
        
        print("正在合成语音...")
        audio_file = synthesize_speech(speech_text)
        
        print("开始播放语音...")
        play_audio(audio_file)

    except Exception as e:
        print(f"程序出错: {e}")

if __name__ == '__main__':
    main()

'''