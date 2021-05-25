import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")


tess.up()                     # this is new
for _ in range(10):    # start with size = 5 and grow by 2
    tess.fd(50)# and turn her
    tess.stamp()                # leave an impression on the canvas in a for loo    p to not write it 10 times
    tess.forward(-50)          # move tess along
    tess.right(36)




wn.exitonclick()
