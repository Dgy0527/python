from aip import AipOcr
from aip import AipSpeech
import os

""" 你的 APPID AK SK """
APP_ID = '1174531'
API_KEY = 'UX8G6WKs0qAtiygBC1nLylsq'
SECRET_KEY = 'pntVHwrfcw7saEQOAYBD23LcCAv9oGaT'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
client1 = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

""" 读取文件 """
def get_file_content(filePath):
    with open(filePath,"rb") as fp:
        return fp.read()

#调用通用文字识别(标准版)
image=get_file_content('药品说明书.jpg')
result=client.basicGeneral(image)
print(result)

#JSON解析开始
txt=''

for i in result['words_result']:
    print(i['words'])
    txt=txt+i['words']

#语音合成
result=client1.synthesis(txt,'zh',1,{
                         'vol':5,
                         })

#识别正确返回语音二进制，识别错误则返回dict,参照下面错误码
if not isinstance(result,dict):
    with open('药品说明书播报.mp3','wb') as f:
        f.write(result)
os.system('药品说明书播报.mp3')


'''
对上面代码的改进:

import os
import sys
from aip import AipOcr, AipSpeech
from dotenv import load_dotenv
import playsound

load_dotenv()

APP_ID = os.getenv('BAIDU_APP_ID')
API_KEY = os.getenv('BAIDU_API_KEY')
SECRET_KEY = os.getenv('BAIDU_SECRET_KEY')

ocr_client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
tts_client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

def ocr_image(image_path):
    try:
        image_data = get_file_content(image_path)
    except FileNotFoundError:
        print(f"错误：文件 {image_path} 不存在")
        return None
    try:
        result = ocr_client.basicGeneral(image_data)
    except Exception as e:
        print(f"OCR请求异常: {e}")
        return None
    if 'error_code' in result:
        print(f"OCR错误: {result['error_msg']}")
        return None
    words_list = result.get('words_result', [])
    if not words_list:
        print("未识别到文字")
        return None
    # 拼接文本（可添加标点）
    text = '。'.join(item['words'] for item in words_list)
    return text

def synthesize_text(text, output_audio='output.mp3'):
    # 注意:百度TTS限制文本长度,若过长可分段处理
    MAX_LEN = 200   # 按需调整
    if len(text) > MAX_LEN:
        print(f"文本过长（{len(text)}字符），仅取前{MAX_LEN}字符")
        text = text[:MAX_LEN]
    try:
        result = tts_client.synthesis(text, 'zh', 1, {'vol': 5})
    except Exception as e:
        print(f"语音合成请求异常: {e}")
        return False
    if isinstance(result, dict):
        print(f"语音合成错误: {result.get('err_msg', '未知错误')}")
        return False
    with open(output_audio, 'wb') as f:
        f.write(result)
    return True

def play_audio(audio_path):
    try:
        playsound.playsound(audio_path)
    except Exception as e:
        print(f"播放音频失败: {e}")

def main():
    if len(sys.argv) < 2:
        print("用法: python script.py <图片路径>")
        return
    image_path = sys.argv[1]
    text = ocr_image(image_path)
    if not text:
        return
    print(f"识别文字: {text[:100]}...")   # 打印预览
    audio_path = f"{os.path.splitext(image_path)[0]}_audio.mp3"
    if synthesize_text(text, audio_path):
        play_audio(audio_path)

if __name__ == '__main__':
    main()

'''