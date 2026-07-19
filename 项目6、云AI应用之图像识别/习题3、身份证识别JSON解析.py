result={'idcard_number_type': 1, 'words_result': {'姓名': {'location': {'top': 41, 'left': 73, 'width': 45, 'height': 20}, 'words': '徐乐'},
        '民族': {'location': {'top': 75, 'left': 148, 'width': 17, 'height': 18}, 'words': '汉'},
        '住址': {'location': {'top': 137, 'left': 70, 'width': 164, 'height': 38},
         'words': '安徽省宿州市埇桥区朱仙庄镇'}, '公民身份号码': {'location': {'top': 217, 'left': 132, 'width': 215, 'height': 18},
        'words': '652901196611026716'}, '出生': {'location': {'top': 105, 'left': 71, 'width': 128, 'height': 18},
        'words': '19661102'}, '性别': {'location': {'top': 75, 'left': 70, 'width': 14, 'height': 18}, 'words': '男'}},
        'words_result_num': 6, 'image_status': 'reversed_side', 'log_id': 2053653013504731044}
print('姓名:',result['words_result']['姓名']['words'])
print('性别:',result['words_result']['性别']['words'])

sfzhm=result['words_result']['公民身份号码']['words']
#print(sfzhm)

year=sfzhm[6:10]
month=sfzhm[10:12]
day=sfzhm[12:14]
print('生日:',year+'年'+month+'月'+day+'日')
print('住址:',result['words_result']['住址']['words'])



'''
对上面代码的改进:

import datetime
import logging

# 配置日志（可选）
logging.basicConfig(level=logging.INFO)

def extract_id_info(result):
    """从OCR结果中安全提取身份证信息"""
    words_result = result.get('words_result', {})
    
    # 1. 检查图片状态
    image_status = result.get('image_status', '')
    if image_status == 'reversed_side':
        logging.warning("图片可能是身份证反面，请确认拍摄方向是否正确。")

    # 2. 安全获取各字段
    name = words_result.get('姓名', {}).get('words', '未识别')
    gender = words_result.get('性别', {}).get('words', '未识别')
    ethnicity = words_result.get('民族', {}).get('words', '未识别')
    address = words_result.get('住址', {}).get('words', '未识别')
    id_number = words_result.get('公民身份号码', {}).get('words', '')

    # 3. 清理地址
    address = address.replace('\n', ' ').strip()

    # 4. 解析出生日期
    birth_date = '未识别'
    if id_number:
        id_number = id_number.strip().upper()
        # 支持15位和18位
        if len(id_number) == 18:
            date_str = id_number[6:14]  # YYYYMMDD
        elif len(id_number) == 15:
            date_str = '19' + id_number[6:12]  # 转换为YYYYMMDD
        else:
            date_str = None

        if date_str:
            try:
                dt = datetime.datetime.strptime(date_str, '%Y%m%d')
                birth_date = dt.strftime('%Y年%m月%d日')
            except ValueError:
                logging.error(f"无效的出生日期: {date_str}")
                birth_date = '日期无效'

    # 5. 输出结果
    print(f"姓名: {name}")
    print(f"性别: {gender}")
    print(f"民族: {ethnicity}")
    print(f"出生日期: {birth_date}")
    print(f"住址: {address}")
    print(f"身份证号: {id_number}")

# 使用示例
if __name__ == '__main__':
    result = {
        'idcard_number_type': 1,
        'words_result': {
            '姓名': {'location': {'top': 41, 'left': 73, 'width': 45, 'height': 20}, 'words': '徐乐'},
            '民族': {'location': {'top': 75, 'left': 148, 'width': 17, 'height': 18}, 'words': '汉'},
            '住址': {'location': {'top': 137, 'left': 70, 'width': 164, 'height': 38},
                     'words': '安徽省宿州市埇桥区朱仙庄镇'},
            '公民身份号码': {'location': {'top': 217, 'left': 132, 'width': 215, 'height': 18},
                          'words': '652901196611026716'},
            '出生': {'location': {'top': 105, 'left': 71, 'width': 128, 'height': 18},
                   'words': '19661102'},
            '性别': {'location': {'top': 75, 'left': 70, 'width': 14, 'height': 18}, 'words': '男'}
        },
        'words_result_num': 6,
        'image_status': 'reversed_side',
        'log_id': 2053653013504731044
    }
    extract_id_info(result)

'''