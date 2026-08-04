#根据空气质量标准(如下图),编写程序,根据PM2.5值,判断空气质量,要求如下:
#1、程序运行时,输入PM2.5值;
#2、输出:根据PM2.5值判断空气质量。


PM=int(input('请输入PM2.5值:'))

if 0<=PM<=35:
    print('空气质量优良')
elif 35<=PM<=75:
    print('空气质量良好')
elif 75<=PM<=115:
    print('空气质量轻度污染')
elif 115<=PM<=150:
    print('空气质量中度污染')
elif 150<=PM<=250:
    print('空气质量深度污染')
elif PM>250:
    print('空气质量重度污染')
else:
    print('请输入正确的PM')

'''
对上面代码的改进:

try:
    pm = float(input('请输入PM2.5值: '))
except ValueError:
    print('输入无效，请输入一个数字！')
else:
    if pm < 0:
        print('PM2.5值不能为负数，请输入正确的数值！')
    elif pm <= 35:          # 0 ~ 35
        print('空气质量优良')
    elif pm <= 75:          # 35 < pm <= 75
        print('空气质量良好')
    elif pm <= 115:         # 75 < pm <= 115
        print('空气质量轻度污染')
    elif pm <= 150:         # 115 < pm <= 150
        print('空气质量中度污染')
    elif pm <= 250:         # 150 < pm <= 250
        print('空气质量重度污染')   # 按常见标准修正为“重度污染”
    else:                   # pm > 250
        print('空气质量严重污染')   # 250以上通常为“严重污染”

'''

#老师的
pm=int(input('请输入PM2.5值:'))

if pm>250:
    kqzl='严重污染'
elif pm>150:
    kqzl='中度污染'
elif pm>115:
    kqzl='轻度污染'
elif pm>75:
    kqzl='良好'
else:
    kqzl='优良'
    
print('空气质量',kqzl)