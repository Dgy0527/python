#画一个多彩五角星

side_num=5
side_length=350
side_angle=180-180/side_num

turtle.speed(6)
turtle.pensize(6)
turtle.color('pink')

turtle.begin_fill()
turtle.forward(side_length)
turtle.left(side_angle)
turtle.color('blue','gray')
turtle.forward(side_length)
turtle.left(side_angle)
turtle.color('green')
turtle.forward(side_length)
turtle.left(side_angle)
turtle.color('yellow')
turtle.forward(side_length)
turtle.left(side_angle)
turtle.color('red','gray')
turtle.forward(side_length)
turtle.left(side_angle)

turtle.end_fill()
turtle.done() #画布不会自动关闭
