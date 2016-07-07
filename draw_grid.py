from turtle import *
from drawman import *
from time import sleep
from math import *

t = Turtle()
x = 0
y = 0
t.speed(100)

def draw_grid(x0, y0,distance):
    global _drawman_scale
    current_color = t.color()
    t.color('grey')
    dx = window_width()/2
    dy = window_height()/2
    distance =_drawman_scale
    goto(-distance,dy)
    t.pendown()
    goto(-distance,-dy)


draw_grid(0,0, 10)
sleep(10)

