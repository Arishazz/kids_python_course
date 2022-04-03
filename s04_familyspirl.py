# SpiralFamily.py - prints a colorful spiral of names

import turtle   
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors=['gainsboro', 'medium aquamarine', 'light coral', 'lavender', 'lavender blush',
        'mint cream', 'white', 'light sea green', 'gray']
family=[]   


name = turtle.textinput("My family",
                        "Enter a name, or press q to stop the programs")

while name != "q":
    
    family.append(name)
   
    name = turtle.textinput("My family",
                        "Enter a name, or press q to stop the program")


for m in range(100):
    t.forward(m*4)
    position = t.position()
    heading = t.heading()   
    for n in range(len(family)):
        t.pendown()
        t.pencolor(colors[n%len(family)%10])
        t.write(family[n%len(family)], font=("Courier", int((m+4)/4), "bold") )
        t.right(360/len(family))
        t.penup()
        t.forward(m//2)
    t.setposition(position)     
    t.setheading(heading)   
    t.left(360/len(family) + 3)  
