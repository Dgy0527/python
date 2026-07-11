#绘制多星环绕
#循环嵌套:一个循环语句在另一个循环语句的内部出现

import turtle
star_num=int(input('想多少颗星环绕呢？'))
side_num=int(input('想画多少角星呢?'))
side_length=int(input('想画多长呢?'))
color_fill=input('想填充什么颜色呢(red,gold,pink)?')

side_angle=180-180/side_num
turtle.pensize(3)
turtle.speed(9)

turtle.begin_fill()

for star in range(star_num):
    for side in range(side_num):
        if side % 5==0:
            side_color='yellow'
        elif side % 5==1:
            side_color='blue'
        elif side % 5==2:
            side_color='pink'
        elif side % 5==3:
            side_color='green'
        else:
            side_color='brown'
        turtle.color(side_color,color_fill)
        turtle.forward(side_length)
        turtle.left(side_angle)
    turtle.left(360/star_num)

turtle.end_fill

turtle.done()


