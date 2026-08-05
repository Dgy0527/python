#有位深圳户籍的白领人员，在深圳奋斗5年了，手头有些存款，他想在深圳购买一套小房子安家。
#于是乎他就去了解深圳购房要求，他了解到自己在深购房只需要首付三成即可，他决定到购房中介了解房价，他所得知房价情况如下表

dic1={
    'count':6,
    'prices':[
        {'name':'顶层小复式','square':45,'pay':16},
        {'name':'低层一居室','square':56,'pay':8},
        {'name':'中层两居室','square':72,'pay':10.5},
        {'name':'中层一居室','square':58,'pay':11},
        {'name':'高层一居室','square':62,'pay':13},
        {'name':'高层小复式','square':45,'pay':15},
    ]
}

name=input('请输入购买的房型:')

for i in dic1['prices']:
    if i['name']==name:
        pay=i['square']*i['pay']*0.3

        print('房型:'+str(i['name']))
        print('首付款:'+str(round(pay,1))+'万元')


'''
对上面代码的改进:

dic1 = {
    'count': 6,
    'prices': [
        {'name': '顶层小复式', 'square': 45, 'pay': 16},
        {'name': '低层一居室', 'square': 56, 'pay': 8},
        {'name': '中层两居室', 'square': 72, 'pay': 10.5},
        {'name': '中层一居室', 'square': 58, 'pay': 11},
        {'name': '高层一居室', 'square': 62, 'pay': 13},
        {'name': '高层小复式', 'square': 45, 'pay': 15},
    ]
}

name = input('请输入购买的房型：').strip()

matched = None
for house in dic1['prices']:
    if house['name'] == name:
        matched = house
        break  # 找到后立即停止

if matched:
    down_payment = matched['square'] * matched['pay'] * 0.3
    print(f"房型：{matched['name']}")
    print(f"首付款：{round(down_payment, 1)}万元")
else:
    print(f"未找到房型“{name}”，请检查输入名称是否准确。")
    print("可选房型有：" + "、".join(h['name'] for h in dic1['prices']))

'''
