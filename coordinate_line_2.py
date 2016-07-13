from turtle import *
from math import *
t = Turtle()
x = 0
y = 0
drawman_scale = 40
t.speed(100)

def calculate_angle(dx, dy):
    if dx > 0:
        return atan(dy/dx)*180/pi
    elif dx < 0:
        if dy > 0:
            return 180 + atan(dy/dx)*180/pi
        else:
            return -180 + atan(dy/dx)*180/pi
    elif dx == 0:
        if dy > 0:
            return 90
        else:
            return -90

def shift(dx, dy):
    global x, y
    x += dx
    y += dy
    angle = calculate_angle(dx, dy)
    length = (dx**2 + dy**2)**0.5
    t.left(angle)
    t.forward(length)
    t.right(angle)

def goto(x1, y1):
    shift(x1 - x, y1 - y)

def coordinate_lines(x0 = 0, y0 = 0):
    current_color = t.color()
    t.color('blue')
    dx = window_width()/2
    dy = window_height()/2
    # x line
    goto(-dx, y0)
    pendown()
    goto(+dx, y0)
    goto(dx - 10, y0 + 10)
    goto(+dx, y0)
    goto(dx - 10, y0 - 10)
    goto(+dx, y0)
    penup()
    # y line
    goto(x0, -dy)
    pendown()
    goto(x0, +dy)
    goto(x0 - 10, dy - 10)
    goto(x0, +dy)
    goto(x0 + 10, dy - 10)
    goto(x0, +dy)
    penup()
    t.color(*current_color)

def draw_grid(x, y):
    global drawman_scale
    distance = drawman_scale
    x0 = 0
    y0 = 0
    current_color = t.color()
    t.color('grey')
    dx = window_width()/2
    dy = window_height()/2
    # x line
    for i in range(1, int(int(dy)/distance)):
        penup()
        goto(-dx, y0+i*distance)
        pendown()
        goto(+dx, y0+i*distance)
        penup()
        goto(-dx, -y0-i*distance)
        pendown()
        goto(+dx, -y0-i*distance)
        penup()
    # y line

    for i in range(1, int(int(dx)/distance)):
        goto(x0+i*distance, -dy)
        pendown()
        goto(x0+i*distance, +dy)
        penup()
        goto(-x0-i*distance, -dy)
        pendown()
        goto(-x0-i*distance, +dy)
        penup()
    t.color(*current_color)

def penup():
    t.penup()

def pendown():
    t.pendown()

def color(col):
    t.color(col)


coordinate_lines(x, y)
draw_grid(x, y)
import time
time.sleep(100)
