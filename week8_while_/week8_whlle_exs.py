# 1
def while_(n):
    counter = 0
    lst = []
    while counter <= n:
        lst.append(counter)
        counter += 1
    return lst


numbers = while_(35)

# 2

L = while_(10)

# 3

nums = while_(20)
# are you fing kidding me, bro????

# 4

# import turtle
# import random
#
# wn=turtle.Screen()
# t=turtle.Turtle()
# # wn.window_height()
# # t.xcor()
# def is_inscreen(wn,t):
#     left_border=-(wn.window_width()/2)
#     right_border=wn.window_width()/2
#     top_border=wn.window_height()/2
#     bot_border=-(wn.window_height()/2)
#
#     turtle_x=t.xcor()
#     turtle_y=t.ycor()
#
#     inscreen=True
#     if turtle_x>right_border or turtle_x<left_border:
#         inscreen=False
#
#     if turtle_y>top_border or turtle_y<bot_border:
#         inscreen=False
#
#     return inscreen
# t.shape("turtle")
# while is_inscreen(wn,t):
#     turn=random.randrange(361)
#     t.rt(turn)
#     t.forward(50)
#
# wn.exitonclick()

# 5

import turtle
import random

wn = turtle.Screen()
t = turtle.Turtle()
leo = turtle.Turtle()


# wn.window_height()
# t.xcor()
def is_inscreen(wn, t):
    left_border = -(wn.window_width() / 2)
    right_border = wn.window_width() / 2
    top_border = wn.window_height() / 2
    bot_border = -(wn.window_height() / 2)

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    inscreen = True
    if turtle_x > right_border or turtle_x < left_border:
        inscreen = False

    if turtle_y > top_border or turtle_y < bot_border:
        inscreen = False

    return inscreen


t.shape("turtle")
randomx = random.randrange(-(wn.window_width() / 2), wn.window_width() / 2)
randomy = random.randrange(-(wn.window_height() / 2), wn.window_height() / 2)
randomxt = random.randrange(-(wn.window_width() / 2), wn.window_width() / 2)
randomyt = random.randrange(-(wn.window_height() / 2), wn.window_height() / 2)
leo.up()
t.penup()
leo.setx(randomx)
leo.sety(randomy)
t.setx(randomxt)
t.sety(randomyt)
leo.pendown()
t.pendown()
while is_inscreen(wn, t) and is_inscreen(wn, leo):
    turn = random.randrange(361)
    turn2 = random.randrange(361)
    leo.rt(turn2)
    t.rt(turn)
    leo.fd(50)
    t.forward(50)

wn.exitonclick()


# 6
def whiletho(n):
    lst = []
    counter = 0
    while counter <= n:
        if counter % 10 == 0:
            lst.append(counter)

        counter += 1
    return lst


tens = whiletho(50)


# 7


def whiletho(n):
    lst = []
    counter = 0
    while counter <= n:
        if counter % 3 == 0:
            lst.append(counter)

        counter += 1
    return lst


three_nums = whiletho(35)
