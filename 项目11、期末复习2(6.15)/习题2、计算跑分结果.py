#1、输入一个整数(范围:700000-880000),
#2、输出所有小于该整数的跑分结果

scores=[810986,725227,871582,805376,805376,739747]
num=eval(input('请输入一个整数(范围:700000-880000):'))

for i in scores:
    if i<num:
        print('跑分结果:',i)


'''
对上面代码的改进:

scores = [810986, 725227, 871582, 805376, 805376, 739747]

while True:
    try:
        num = int(input('请输入一个整数(范围:700000-880000): '))
        if 700000 <= num <= 880000:
            break
        print('输入不在范围内，请重新输入。')
    except ValueError:
        print('输入无效，请输入一个整数。')

# 去重，避免重复输出相同分数
unique_scores = sorted(set(scores), reverse=True)

has_result = False
for score in unique_scores:
    if score < num:
        print('跑分结果:', score)
        has_result = True

if not has_result:
    print(f'没有小于 {num} 的跑分结果。')

'''