import turtle as t
from random import randint, random


# size = 350
# points = 666
# angle = 180 - (180 / points)

# t.color('red')
# t.begin_fill()

# for i in range(points):
#     t.forward(size)
#     t.right(angle)

# t.end_fill()

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()



t.Screen().bgcolor('dark blue')
while True:
    ranSpeed = randint(100, 200)
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(10, 50)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
    t.speed(ranSpeed)

t.exitonclick()