import turtle
import random
lst=[160, -43, 270, -97, -43, 200, -940, 17, -86]
numba=0
t=turtle.Turtle()
t.speed(0)
wn=turtle.Screen()
for i in lst:
    # rand=random.randint(-940,270)
    numba=(numba+i)%360
    # print(numba)
    t.lt(i)
    t.fd(100)
print(numba)
print(t.heading())
wn.exitonclick()