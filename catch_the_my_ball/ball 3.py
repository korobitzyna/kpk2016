import tkinter
from random import choice, randint


ball_initial_number = 20
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']
ball_recruited_sum = 1
ball_speed_decrease = 1
ball_speed_increases = 1

def click_ball(event):
    """ Обработчик событий мышки для игрового холста canvas
    :param event: событие с координатами клика
    По клику мышкой нужно удалять тот объект, на который мышка указывает.
    А также засчитываеть его в очки пользователя.
    """
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        create_random_ball()
        # FIXME: генератор шариков сделать зависимым от набранной суммы
        ball_sum() # счетчик собранных шариков
        # FIXME: нужно учесть объект в очках

def ball_sum():
    # подсчет баллов
    global ball_recruited_sum
    ball_recruited_sum += 1


def move_all_balls(event):
    """ передвигает все шарики на чуть-чуть
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)

def create_random_ball():
    """
    создаёт шарик в случайном месте игрового холста canvas,
     при этом шарик не выходит за границы холста!
    """
    global ball_speed_decrease
    for i in range(ball_speed_decrease):
        R = randint(ball_minimal_radius, ball_maximal_radius)
        x = randint(0, int(canvas['width'])-1-2*R)
        y = randint(0, int(canvas['height'])-1-2*R)
        canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())



def random_color():
    """
    :return: Случайный цвет из некоторого набора цветов
    """
    return choice(ball_available_colors)


def init_ball_catch_game():
    """
    Создаём необходимое для игры количество шариков, по которым нужно будет кликать.
    """
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root, canvas, label

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()
    label = tkinter.Label(root, text=ball_recruited_sum, font="Arial 12")
    label.pack()
    canvas.pack()

def init_window_2():
    global root2, canvas2, label2, ball_recruited_sum, scala

    root2 = tkinter.Toplevel()
    canvas2 = tkinter.Canvas(root2, background='white', width=400, height=400)
    variable = tkinter.IntVar(int(ball_recruited_sum/10))
    label2 = tkinter.Label(root2, textvariable=variable)
    scale = tkinter.Scale(root2, orient=tkinter.HORIZONTAL, length=300,
                          from_=0, to=10, tickinterval=1, resolution=0.5, variable=variable)
    text = tkinter.Entry(root2, textvariable=variable)

    for obj in  label2, scale, text:
        obj.pack()


if __name__ == "__main__":
    init_main_window()
    init_window_2()
    init_ball_catch_game()
    root2.mainloop()
    root.mainloop()
    print("Приходите поиграть ещё! Вы набрали", ball_recruited_sum, "баллов")