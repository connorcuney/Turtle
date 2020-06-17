import turtle
import random


def circle(cr, size, times):
    for i in range(times):
        cr.circle(size)
        cr.right(360/times)


screen = turtle.Screen()
cursor = turtle.Turtle()

screen.colormode(255)
cursor.speed(0)
cursor.pensize(6)

for i in range(1, 10):
    cursor.pencolor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    screen.bgcolor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    circle(cursor, 20*i, 10)

cursor.hideturtle()
turtle.done()

