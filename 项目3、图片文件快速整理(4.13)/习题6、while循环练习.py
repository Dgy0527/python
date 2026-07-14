#while循环练习
#1、for循环:遍历循环;while循环:条件循环
#2、while循环:只要条件为真,循环会一直执行下去;while条件:循环体(语句块)
#3、无限循环:只要条件为真,循环就会一直执行下去,或称为死循环
#4、循环控制语句:break:循环终止 continue:本次循环结束,跳到下一次循环

while True:
    score=int(input('请输入学生的成绩:'))
    if score>100 or score<0:
        print('你输入的成绩有误:退出了')
        #break
        continue