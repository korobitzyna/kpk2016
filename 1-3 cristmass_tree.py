from drawman import *

def cristmass_tree(height):
    penup()
    x0, y0 = x, y
    print(x, y)
    shift(0, height)
    pendown()
    slide_height = height/5
    for level in range(5):
        shift(slide_height, -slide_height)
        shift(-slide_height/1.5, 0)
    goto(x0, y0)
    print(x, y)
    penup()
    shift(0, height)
    pendown()
    for level in range(5):
        shift(-slide_height, -slide_height)
        shift(slide_height/1.5, 0)
    goto(x0, y0)
    penup()
for tree in range(1, 6):
    cristmass_tree(40*tree)