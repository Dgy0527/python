#统计三位数里有多少个符合条件的数字,条件如下:十位数是1或个位数是2

count=0
print('符合条件的三位数是:')

for num in range(100,999+1):
    if (num//10%10==1) or (num%10==2):
        print(num)
        count+=1
print('总个数是:',count)



'''
豆包给的

result=[]
for num in range(100,1000):
    tens=num // 10 % 10
    units=num % 10

    if tens==1 or units==2:
        result.append(str(num))

print('符合条件的三位数是:')
print(' '.join(result))
print(f'总个数是:{len(result)}')



豆包对自己的改进:

1、每行打印多个数字

result = []
for num in range(100, 1000):
    tens = num // 10 % 10
    units = num % 10
    if tens == 1 or units == 2:
        result.append(str(num))

print('符合条件的三位数是:')
# 每行打印10个数字(可根据需要调整)
for i in range(0, len(result), 10):
    print(' '.join(result[i:i+10]))
print(f'总个数是: {len(result)}')


2、优化输出格式

count = 0
print('符合条件的三位数是:')

# 用列表存储，但为了展示每行多个，可以临时拼接字符串
result = []
for num in range(100, 1000):
    tens = num // 10 % 10
    units = num % 10
    if tens == 1 or units == 2:
        result.append(str(num))
        count += 1

# 每行打印 10 个数字，便于阅读
for i in range(0, len(result), 10):
    print(' '.join(result[i:i+10]))

print(f'总个数是: {count}')

'''