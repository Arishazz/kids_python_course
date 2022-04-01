import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = eval( input("How many sides would you like between 1 and 12?") )
colors = ["red", "yellow", "blue", "orange", "green", "purple",
          "pink", "salmon", "maroon", "violet", "powder blue", "indigo"]
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.right(360/sides + 3)
    t.width(x*sides/200)
    t.right(90)
