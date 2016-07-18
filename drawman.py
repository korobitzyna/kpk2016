from turtle import Turtle
from math import *

default_scale = 40
x = 0
y = 0

def init_drawman():
    global t, x_current, y_current, _drawman_scale, dx, dy
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    dx = t.screen.window_width()/2
    dy = t.screen.window_height()/2
    t.goto(x_current, y_current)
    drawman_scale(default_scale)


def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale


def test_drawman():
    """
    Тестирование работы Чертёжника
    :return: None
    """
    pen_down()
    for i in range(5):
        on_vector(10, 20)
        on_vector(0, -20)
    pen_up()
    to_point(0, 0)


def pen_down():
    t.pendown()


def pen_up():
    t.penup()


def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)


def to_point(x, y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(_drawman_scale*x_current, _drawman_scale*y_current)

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


def drawman_goto(x1, y1):
    shift(x1 - x, y1 - y)


def coordinate_lines(x0 = 0, y0 = 0):
    current_color = t.color()
    t.color('blue')
    # x line
    drawman_goto(-dx, y0)
    pen_down()
    drawman_goto(+dx, y0)
    drawman_goto(dx - 10, y0 + 10)
    drawman_goto(+dx, y0)
    drawman_goto(dx - 10, y0 - 10)
    drawman_goto(+dx, y0)
    pen_up()
    # y line
    drawman_goto(x0, -dy)
    pen_down()
    drawman_goto(x0, +dy)
    drawman_goto(x0 - 10, dy - 10)
    drawman_goto(x0, +dy)
    drawman_goto(x0 + 10, dy - 10)
    drawman_goto(x0, +dy)
    pen_up()
    t.color(*current_color)

def draw_grid(x0 = 0, y0 = 0):
    distance = _drawman_scale
    current_color = t.color()
    t.color('grey')
    # x line
    for i in range(1, int(int(dy)/distance)):
        pen_up()
        drawman_goto(-dx, y0+i*distance)
        pen_down()
        drawman_goto(+dx, y0+i*distance)
        pen_up()
        drawman_goto(-dx, -y0-i*distance)
        pen_down()
        drawman_goto(+dx, -y0-i*distance)
        pen_up()
    # y line

    for i in range(1, int(int(dx)/distance)):
        drawman_goto(x0+i*distance, -dy)
        pen_down()
        drawman_goto(x0+i*distance, +dy)
        pen_up()
        drawman_goto(-x0-i*distance, -dy)
        pen_down()
        drawman_goto(-x0-i*distance, +dy)
        pen_up()
    t.color(*current_color)


init_drawman()

if __name__ == '__main__':
    import time
    test_drawman()
    time.sleep(10)