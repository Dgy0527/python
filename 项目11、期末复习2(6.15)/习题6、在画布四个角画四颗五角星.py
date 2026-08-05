'''
通过turtle库,在画布的四个角分别画出位置,边长和颜色可指定的五角星
1、函数的概念:是组织好的,可重复使用的,用来实现单一或相关联功能的代码段
2、函数的功能:能提高程序的可读性和代码的重复利用率
3、函数的定义:函数的语法格式:def 函数名(形参1、形参2、形参3......):函数代码块(函数体)
4、函数的调用:函数调用语法格式:函数名(实参1、实参2、实参3......)
'''

import turtle

def star(x,y,length,color): #4用法
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(5):
        turtle.forward(length)
        turtle.left(180-180/5)
    turtle.end_fill()

#函数开始调用
turtle.setup(500,500)
color='red'
turtle.speed(10)
star(-250,220,50,color)
star(-250,-220,50,color)
star(190,220,50,color)
star(190,-220,50,color)

turtle.done()


'''
对上面代码的改进:

import turtle

def star(x, y, length, color):
    """
    在指定坐标画一个给定边长和颜色的五角星
    参数:x横坐标, y纵坐标, length边长, color颜色
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    # 统一将画笔朝向调整为垂直向上(90度),确保所有星星的尖端都朝上
    turtle.setheading(90)

    # 设置画笔颜色和填充颜色为同一种
    turtle.color(color, color) 
    turtle.begin_fill()

    for i in range(5):
        turtle.forward(length)
        turtle.left(144)  # 五角星的标准外转角为144度

    turtle.end_fill()

# --- 主程序调用 ---
turtle.setup(500, 500)
turtle.speed(10)

# 为了让星星能完整显示在画布内，不让它贴死边缘，我们使用 ±180 作为四角坐标
star(-180, 180, 50, "red")    # 左上角
star(180, 180, 50, "blue")    # 右上角
star(-180, -180, 50, "green") # 左下角
star(180, -180, 50, "gold")   # 右下角

# 隐藏海龟画笔，让最后画面更整洁
turtle.hideturtle()
turtle.done()

'''