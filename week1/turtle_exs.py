# # 1
# for _ in range(100):
#     print("We love Python's turtles!")
#
# import turtle
#
# wn=turtle.Screen()
# leo=turtle.Turtle()
#
# 3
# for _ in range(3):
#     leo.forward(50)
#     leo.lt(120)
# for _ in range(4):
#     leo.forward(50)
#     leo.lt(90)
# for _ in range(6):
#     leo.forward(50)
#     leo.lt(60)
# for _ in range(8):
#     leo.forward(50)
#     leo.lt(45)
#
#
# #4
# for _ in range(5):
#     leo.rt(145)
#     leo.fd(100)
# #5
# wn.bgcolor("lightgreen")
# leo.shape("turtle")
# leo.color("blue")
#
# leo.up()
# for _ in range(12):
#     leo.fd(75)
#     leo.down()
#     leo.fd(10)
#     leo.up()
#     leo.fd(15)
#     leo.stamp()
#     leo.fd(-100)
#     leo.lt(30)
#


import turtle

wn = turtle.Screen()
leo = turtle.Turtle()
leo.pensize(2)
leo.speed(0)

alexey = turtle.Turtle()
alexey.pensize(2)
alexey.speed(0)

leo.up()
leo.bk(100)
leo.down()
# bar of the dumbell
for i in range(2):
    leo.fd(200)
    leo.rt(90)
    leo.fd(20)
    leo.rt(90)

dist = 100
# prep for the weights
leo.rt(90)
leo.up()
leo.fd(10)
leo.down()


# weights1
def turtlee(dist, leo):
    leo.fd(dist / 2)
    leo.rt(90)
    leo.fd(dist / 5)
    leo.rt(90)
    leo.fd(dist)
    leo.rt(90)
    leo.fd(dist / 5)
    leo.rt(90)
    leo.fd(dist / 2)


# weights2
def turtlee1(dist, leo):
    leo.up()

    leo.rt(90)
    leo.fd(dist / 5)
    dist -= 20

    leo.fd(dist / 5)
    leo.rt(90)
    leo.down()


# drawing the 3 weights
turtlee(dist, leo)
turtlee1(dist, leo)
turtlee(dist - 20, leo)
leo.rt(180)
turtlee(dist - 40, leo)

leo.hideturtle()

# prep for the weights
alexey.fd(100)
alexey.lt(90)

alexey.fd(-10)


# drawing the 3 weights
turtlee(dist, alexey)
turtlee1(dist, alexey)
turtlee(dist - 20, alexey)
alexey.rt(180)
turtlee(dist - 40, alexey)

alexey.hideturtle()

wn.exitonclick()

# 7
print(leo)
