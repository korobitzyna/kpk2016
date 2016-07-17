import tkinter
from random import choice, randint


ball_initial_number = 20
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']
ball_recruited_sum = 0
ball_speed_decrease = 0
def click_ball(event):
    """ Обработчик событий мышки для игрового холста canvas
    :param event: событие с координатами клика
    По клику мышкой нужно удалять тот объект, на который мышка указывает.
    А также засчитываеть его в очки пользователя.
    """
    global ball_maximal_radius, ball_speed_decrease
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        create_random_ball()
        ball_maximal_radius -= 1 #максимальный радиус шарика уменьшается
        if ball_minimal_radius >= ball_maximal_radius:
            ball_speed_decrease -= 1 #скорость появления шариков уменьшается
        else:
            ball_speed_decrease += 1 #скорость появления шариков увеличивается
        ball_sum() # счетчик собранных шариков

def ball_sum():
    # подсчет суммы баллов
    global ball_recruited_sum
    ball_recruited_sum += 1


def move_all_balls(event):
    """ передвигает все шарики на чуть-чуть НО выходят за границы холста
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)

def create_random_ball():
    """
    создаёт шарик в случайном месте игрового холста canvas,
     при этом шарик не выходит за границы холста
    """
    global ball_speed_decrease,  ball_minimal_radius, ball_maximal_radius
    for i in range(ball_speed_decrease+1):
        if ball_minimal_radius >= ball_maximal_radius:
            ball_minimal_radius, ball_maximal_radius = ball_maximal_radius, ball_minimal_radius
        else:
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
    canvas.pack()

def init_window_2():
    global root2, canvas2, label2, label3,ball_recruited_sum, scala

    root2 = tkinter.Toplevel()
    label2 = tkinter.Label(root2, text="Приходите поиграть ещё!")
    label3_text = "Вы набрали " + str(ball_recruited_sum) +" баллов"
    label3 = tkinter.Label(root2, text=label3_text)
    label4_text = "Максимальный радиус " + str(ball_maximal_radius)
    label4 = tkinter.Label(root2, text=label4_text)
    for obj in label2, label3, label4:
        obj.pack()
    root2.mainloop()

def game_over():
    # выводит итог игры
    global ball_recruited_sum, ball_maximal_radius
    init_window_2()
    print("Приходите поиграть ещё!")
    print("Вы набрали", ball_recruited_sum, "баллов")
    print("максимальный радиус", ball_maximal_radius)
    exit()


if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    game_over()