# CircleSpiral.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colours = ["red", "blue", "violet", "salmon"]
t.speed(0)
for x in range(450):
    t.pencolor( colours[ x % 4])
    t.circle(x)
    t.left(46)
