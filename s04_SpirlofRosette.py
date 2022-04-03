# ViralSpiral.py - a spiral of spirals!
import turtle
t = turtle.Pen()
t.speed(0)
t.width(0)
t.penup()
turtle.bgcolor("black")
# Ask the user for the number of sides, default to 4, min 2, max 6
circles = int(turtle.numinput("Number of circles",
            "How many sides would you like in your spiral of rosettes?? (2-6)", 4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
# Our outer spiral loop
for m in range(100):
    t.forward(m*4)
    position = t.position() # Remember this corner of the spiral
    heading = t.heading()   # Remember the direction we were heading
    print(position, heading)
    # Our "inner" spiral loop
    # Draws a little spiral at each corner of the big spiral
    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%circles])
        t.circle(m/5)
        t.right(360/circles)
        t.penup()
    t.setpos(position)      # Go back to the big spiral's x location
    t.setheading(heading)   # Point in the big spiral's heading
    t.left(360/circles + 2)   # Aim at the next point on the big spiral

