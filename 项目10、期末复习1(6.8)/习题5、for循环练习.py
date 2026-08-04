#求1^2-2^2+3^2-4^2+...+9^2-10^2的值

sum=0

for i in range(1,11):
    if i%2==1:
        sum=sum+i**2
    else:
        sum=sum-i**2
        
print(sum) 