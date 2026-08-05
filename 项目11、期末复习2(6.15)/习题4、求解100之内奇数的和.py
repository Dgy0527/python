#求100之内奇数的和

sum=0

for i in range(1,101):
    if i%2==1:
        sum=sum+i

print('1到100之间的奇数的和为:',sum)


'''
对上面代码的改进:

# 方案一:使用步长，保留手动累加（重命名变量）
total = 0
for i in range(1, 101, 2):
    total += i
print('1到100之间的奇数的和为:', total)

# 方案二:Pythonic 写法，直接利用 sum() 内置函数
odd_sum = sum(range(1, 101, 2))
print('1到100之间的奇数的和为:', odd_sum)

'''