text='''民族要复兴，乡村必振兴
实施乡村振兴战略是党和国家的重大战略部署，是一篇全面振兴的大文章。
在这一战略中，农业农村现代化是总目标，坚持农业农村优先发展是总方针，
产业兴旺、生态宜居、乡风文明、治理有效、生活富裕是总要求，
建立健全城乡融合发展体制机制和政策体系是制度保障。
'''

from aip import AipSpeech
import os

"""你的 APPID AK SK"""
APP_ID = '11437531'
API_KEY = 'UX8G6WKs0qAtlhgBC1nLylsq'
SECRET_KEY = 'pntVHwrfcwASqEQOAYBD23LcCAv9oGaT'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result=client.synthesis(text,'zh',1,{
    'vol':5,
})

#识别正确返回语音二进制,错误则返回dict,参考下面错误码
if not isinstance(result,dict):
    with open('audio.mp3','wb') as f:
        f.write(result)
os.system('audio.mp3')




'''
上面代码存在的问题:1、os.system() 在windows上调用默认播放器
                  2、密钥直接写在代码里面

对上面代码的改进:1、使用.env文件保存密钥

import os
import sys
from dotenv import load_dotenv
from aip import AipSpeech

# 1. 加载 .env 文件中的密钥
load_dotenv() #pip install python-dotenv playsound

APP_ID = os.environ.get('BAIDU_APP_ID')
API_KEY = os.environ.get('BAIDU_API_KEY')
SECRET_KEY = os.environ.get('BAIDU_SECRET_KEY')

if not all([APP_ID, API_KEY, SECRET_KEY]):
    sys.exit(
        '请先设置环境变量，或在脚本同目录创建 .env 文件，写入:\n'
        'BAIDU_APP_ID=你的APP_ID\n'
        'BAIDU_API_KEY=你的API_KEY\n'
        'BAIDU_SECRET_KEY=你的SECRET_KEY'
    )

# 2. 初始化百度语音客户端
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def tts_and_play(text, vol=8, spd=5, pit=5, per=0):
    """
    使用百度语音合成，并调用系统默认播放器播放。
    """
    result = client.synthesis(text, 'zh', 1, {
        'vol': vol,
        'spd': spd,
        'pit': pit,
        'per': per,
    })

    # 判断是否合成出错
    if isinstance(result, dict):
        err_no = result.get('err_no', '')
        err_msg = result.get('err_msg', '未知错误')
        print(f'语音合成失败，错误码：{err_no}，原因：{err_msg}')
        return False

    # 写入当前目录的 output.mp3
    output_file = 'output.mp3'
    with open(output_file, 'wb') as f:
        f.write(result)
    print(f'语音已合成，文件路径：{os.path.abspath(output_file)}')

    # 调用系统默认程序播放
    try:
        if sys.platform == 'win32':
            os.system(f'start "" "{output_file}"')
        elif sys.platform == 'darwin':
            os.system(f'afplay "{output_file}"')
        else:
            os.system(f'xdg-open "{output_file}"')
    except Exception as e:
        print(f'无法自动播放，请手动打开 {output_file}，错误信息：{e}')

    return True


# 3. 主程序入口
if __name__ == '__main__':
    news_text = (
        '民族要复兴，乡村必振兴。'
        '实施乡村振兴战略是党和国家的重大战略部署，是一篇全面振兴的大文章。'
        '在这一战略中，农业农村现代化是总目标，坚持农业农村优先发展是总方针，'
        '产业兴旺、生态宜居、乡风文明、治理有效、生活富裕是总要求，'
        '建立健全城乡融合发展体制机制和政策体系是制度保障。'
    )

    print('开始合成语音...')
    ok = tts_and_play(news_text, vol=10, per=0)
    if not ok:
        sys.exit(1)
    print('播放完毕（若播放器未弹出，请检查同目录下的 output.mp3)')

'''