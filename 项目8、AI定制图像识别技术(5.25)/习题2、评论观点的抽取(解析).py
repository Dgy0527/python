result={'log_id':3185339167615696940021,
        'items':
        [
            {'sentiment': 2, 'abstract': '这个彩色的看着好看就买了', 'prop': '感觉', 'begin_pos': 24, 'end_pos': 24, 'adj': '好看'},
            {'sentiment': 2, 'abstract': '二维码识别还是比较快的', 'prop': '速度', 'begin_pos': 22, 'end_pos': 22, 'adj': '快'}
        ]

}

#解析开始
for i in result['items']:
    if i['sentiment']==2:
        print('\n极性:积极')
        print('属性词:',i['prop'])
        print('描述词:',i['adj'])
    elif i['sentiment']==1:
        print('\n极性:中性')
        print('属性词:',i['prop'])
        print('描述词:',i['adj'])
    else:
        print('\n极性:消极')
        print('属性词:',i['prop'])
        print('描述词:',i['adj'])