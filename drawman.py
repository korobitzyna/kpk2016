from turtle import Turtle
default_scale = 10

def init_drawman():
    global t, x_current, y_current, _drawman_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
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

def calculate_angle(dx, dy):    # стрелка для оси ОХ
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

def shift(dx, dy):            # диагональ для первой координатной четверти
    global x, y
    x += dx
    y += dy
    angle = calculate_angle(dx, dy)
    length = (dx**2 + dy**2)**0.5
    t.left(angle)
    t.forward(length)
    t.right(angle)

init_drawman()
if __name__ == '__main__':
    import time
    test_drawman()
    time.sleep(10)
