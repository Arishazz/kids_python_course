# ColorSpiralInput.py
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
# Set up a list of any 8 valid Python color names
colors = ["red", "yellow", "blue", "green",
          "orange", "purple", "white", "gray"]
# Ask the user for the number of circles
sides = int( turtle.numinput("Number of circles",
                             "How many circles would you like (1-8)?", 4, 1, 8))
# Draw a colorful spiral with the user-specified number of circles
for x in range(360):
    t.pencolor( colors[x % sides] )
    t.circle( x * 3 / sides + x)
    t.left(90)
    t.width(x * sides / 200)
    
    
