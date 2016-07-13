from turtle import *
from drawman import *
from time import sleep
from math import *

t = Turtle()
x = 0
y = 0
t.speed(100)

def draw_grid(x0, y0):
    current_color = t.color()
    t.color('grey')
    dx = window_width()/2
    dy = window_height()/2
    # x line
    for i in range(int(dy/10)):
        penup()
        goto(-dx, y0+10*i)
        pendown()
        goto(+dx, y0+10*i)
        penup()
        goto(-dx, -y0-10*i)
        pendown()
        goto(+dx, -y0-10*i)
        penup()
    # y line

    for i in range(int(dx/10)):
        goto(x0+10*i, -dy)
        pendown()
        goto(x0+10*i, +dy)
        penup()
        goto(-x0-10*i, -dy)
        pendown()
        goto(-x0-10*i, +dy)
        penup()
    t.color(*current_color)

def penup():
    t.penup()

def pendown():
    t.pendown()

def color(col):
    t.color(col)

draw_grid(10, 10)
coordinate_lines(x, y)
import time
time.sleep(100)

