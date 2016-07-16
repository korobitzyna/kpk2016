import tkinter
from random import choice, randint

ball_initial_number = 20
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']
ball_recruited_sum = 0

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
        ball_recruited_sum += 1
        # FIXME: нужно учесть объект в очках
        create_random_ball()


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
    global root, canvas

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()

def button1_command():
    #обработка событий кнопки 1
    print('Button 1 default command.')


def print_hello(event):
    #обработка событий кнопки м1 и кнопки 2
    print(event.num)
    print(event.x, event.y)
    #print(event.x_root, event.y_root)
    me = event.widget
    # что можно сделать с me?
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('You pressed button 2!')
    else:
        raise ValueError()
def init_main_window2():
    """
 Инициализация второго окна: создание всех необходимых виджетов и их упаковка.
 :return:
    """
    global root2, button1, button2, label, text, scale

    root2 = tkinter.Tk()

    button1 = tkinter.Button(root2, text="Button 1", command=button1_command)
    button1.bind("<Button>", print_hello)

    button2 = tkinter.Button(root2, text="Button 2")
    button2.bind("<Button>", print_hello)

    variable = tkinter.IntVar(0)
    label = tkinter.Label(root2, textvariable=variable)
    scale = tkinter.Scale(root2, orient=tkinter.HORIZONTAL, length=300,
                          from_=0, to=100, tickinterval=10, resolution=5, variable=variable)
    text = tkinter.Entry(root2, textvariable=variable)

    for obj in button1, button2, label, scale, text:
        obj.pack()


if __name__ == "__main__":
    init_main_window()
    init_main_window2()
    init_ball_catch_game()
    root.mainloop()
    print("Приходите поиграть ещё!")