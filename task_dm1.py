from drawman import *
from time import sleep

A = [(0, 0), (10, 0), (10, 10), (0, 10)]

pen_down()
for x, y in A:
    to_point(x, y)
to_point(A[0][0], A[0][1])
pen_up()

sleep(20)