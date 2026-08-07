'''
18、
太阳系八大行星的顺序是水星-金星-地球-火星-木星-土星-天王星-海王星。
名称	直径(千米)
水星	4878
金星	12103
地球	12756
火星	6786
木星	142984
土星	120536
天王星	51118
海王星	49528

现请你使用以下字典，设计一个如下的程序（参考程序说明）：

1.planet = {
2.    'count': 7,
3.    'volume': [
4.        {'name': '水星', 'diameter': 4878},
5.        {'name': '金星', 'diameter': 12103},
6.        {'name': '地球', 'diameter': 12756},
7.        {'name': '火星', 'diameter': 6786},
8.        {'name': '木星', 'diameter': 142984},
9.        {'name': '土星', 'diameter': 120536},
10.        {'name': '天王星', 'diameter': 51118},
11.        {'name': '海王星', 'diameter': 49528}
12.    ]
13.}

程序说明
1.输入行星名称
2.输出该行星体积
注：:(计算公式:(体积=4/3x3.14xR3))

样例输入
请输入行星名称：地球
样例输出
地球体积为:1086230340743039.9立方米

'''

planet = {
    'count': 7,
    'volume': [
        {'name': '水星', 'diameter': 4878},
        {'name': '金星', 'diameter': 12103},
        {'name': '地球', 'diameter': 12756},
        {'name': '火星', 'diameter': 6786},
        {'name': '木星', 'diameter': 142984},
        {'name': '土星', 'diameter': 120536},
        {'name': '天王星', 'diameter': 51118},
        {'name': '海王星', 'diameter': 49528}
    ]
}

name1=input('请输入行星名称:')

for i in planet['volume']:
    if i['name']==name1:
        num=4/3*3.14*(i['diameter']/2)**3*1000
        print(name1+'体积为:'+str(num)+'立方米')


'''
对上面代码的改进:

import math  # 可选,但为保持样例一致,此处仍用3.14

planet = {
    'count': 8,  # 修正为8
    'volume': [
        {'name': '水星', 'diameter': 4878},
        {'name': '金星', 'diameter': 12103},
        {'name': '地球', 'diameter': 12756},
        {'name': '火星', 'diameter': 6786},
        {'name': '木星', 'diameter': 142984},
        {'name': '土星', 'diameter': 120536},
        {'name': '天王星', 'diameter': 51118},
        {'name': '海王星', 'diameter': 49528}
    ]
}

name_input = input("请输入行星名称：").strip()

# 查找行星
target_planet = None
for p in planet['volume']:
    if p['name'] == name_input:
        target_planet = p
        break

if target_planet is None:
    print(f"错误：未找到行星“{name_input}”，请确认名称输入正确。")
else:
    # 计算体积（直径单位：千米）
    radius = target_planet['diameter'] / 2
    volume_km3 = 4 / 3 * 3.14 * radius ** 3
    # 转换为立方米(保留与样例一致的转换系数1000,实际应为1e9)
    volume_m3 = volume_km3 * 1000  # 根据样例保持一致
    # 格式化输出,保留1位小数
    print(f"{name_input}体积为:{volume_m3:.1f}立方米")

'''