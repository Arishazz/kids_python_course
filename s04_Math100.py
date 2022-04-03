# SayOurNames.py - lets everybody print their name on the screen
equation = eval(input("What is your equation?"))
while equation != " ":
    for x in range(100):
        print("The answer is", equation, end = ". ")
    print() 
    equation = input("Ask again, or just hit [ENTER] to quit: ")
print("Thanks for playing!")

