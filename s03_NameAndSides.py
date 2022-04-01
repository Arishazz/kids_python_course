# SpiralMyName.py - prints a colorful spiral of the user's name

import turtle               # Set up turtle graphics
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("light salmon")
colors = ["light pink", "peach puff", "light blue", "pale green"]

# Ask the user's name using turtle's textinput pop-up window
your_name = turtle.textinput("Enter your name", "What is your name?")
sides = int(turtle.numinput("# of sides", "How many sides would you like from 1-4?", 2, 1, 4))

# Draw a spiral of the name on the screen, written 100 times
for x in range(100):
    t.pencolor( colors[ x % sides] )
    t.penup()
    t.forward( x * sides )
    t.pendown()
    t.write(your_name, font = ("Courier", int( (x + sides) / sides), "bold") )
    t.left(360/sides + sides)
    
    



