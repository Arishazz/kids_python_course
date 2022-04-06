#RandomSpirals.py
import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["light salmon", "lavender", "lavender blush", "pastel orange",
          "white", "gray"]

for n in range(50):
    # Generate spirals of random sizes/colors at random locations
    t.pencolor(random.choice(colors))   # Pick a random color 
    size = random.randint(10,40)        # Pick a random spiral size
    # Generate a random (x,y) location on the screen
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.circle(size)
        t.left(45)
        

