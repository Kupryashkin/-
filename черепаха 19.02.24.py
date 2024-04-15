# Задание 1
import turtle
t = turtle.Turtle()
t.speed(10)
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done()

# Задание  2
import turtle
t = turtle.Turtle()
t.speed(10)
t.goto(0,0)
t.goto(124,0)
t.goto(56,32)
t.goto(0,0)
turtle.done()

# Задание 3
import turtle
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor('red')
t.circle(80)
turtle.done()

# Задание 4
import turtle
t = turtle.Turtle()
a = 150
b = 90
turtle.circle(a,45)
turtle.circle(b,90)
turtle.circle(a,90)
turtle.circle(b,90)
turtle.circle(a,45)

# Задание 5
import turtle
t = turtle.Turtle()
t.speed(10)

t.color('blue')
t.fillcolor('blue')

t.begin_fill()
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()
turtle.done()

# цент не получилось закрасить

# Задание 6
import turtle
colors = ['green', 'red', 'yellow', 'black']
t = turtle.Turtle()
t.speed(0)
for i in range(12):
    color = colors[i %  len(colors)]
    t.pencolor(color)
    t.circle(50)
    t.penup()
    t.right(30)
    t.pendown()

turtle.done()

# Задание 7
import turtle
t.turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()



# Задание 8
import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(190)
    t.right(90)
    t.color('black')
    t.write('Hello World!', False, align='left', font=('Arial', 10, 'normal'))
    t.speed(10)
turtle.done
