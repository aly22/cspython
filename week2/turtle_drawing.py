import turtle
n=int(input("the number of sides of the polygon: "))
n2=int(input("the length of the side: "))
c=input("The color of the side: ")
c2=input("the fill color: ")
t=turtle.Turtle()
t.speed(0)
wn=turtle.Screen()
t.color(c)
t.begin_fill()
t.fillcolor(c2)
for _ in range(n):
    t.fd(n2)
    t.lt(360/n)
t.end_fill()
wn.exitonclick()

