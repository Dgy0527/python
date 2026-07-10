#绘制一个等边三角形
import turtle

turtle.speed(6)
turtle.pensize(6)
turtle.color('pink','gray')

turtle.begin_fill()
turtle.forward(400)
turtle.left(120)
turtle.forward(400)
turtle.left(120)
turtle.forward(400)
turtle.left(120)
turtle.end_fill()

turtle.done() #画布不会自动关闭
