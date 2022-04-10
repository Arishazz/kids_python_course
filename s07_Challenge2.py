# PingPong_Calculator.py

def convert_in2cm(inches):
    return inches * 2.54
def convert_lb2kg(pounds):
    return pounds / 2.2

print("Use this program to see how tall and heavy ping pong balls are!!")
pingPongs = int(input("Enter a number!"))



height = round(pingPongs * 4)
weight = round(pingPongs * 2.7)




print(pingPongs, "ping pong balls would be", height, "cm tall, and weigh", weight, "g")


