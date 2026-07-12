#绘制多彩多角星
import turtle

side_num=7
side_length=450
side_angle=180-180/side_num
turtle.pensize(9)
turtle.speed(10)
color_fill='gold'

turtle.begin_fill()
for side in range(side_num):
    if side % 5==0:
        side_color='yellow'
    elif side % 5==1:
        side_color='blue'
    elif side % 5==2:
        side_color=='pink'
    elif side % 5==3:
        side_color='green'
    else:
        side_color='brown'

    turtle.color(side_color,color_fill)
    turtle.forward(side_length)
    turtle.left(side_angle)
    turtle.end_fill()

turtle.done()