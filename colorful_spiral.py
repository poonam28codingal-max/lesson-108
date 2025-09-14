import turtle
import random

screen = turtle.Screen()
screen.title("Colorful Spiral - Random Colors")
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)            # fastest
t.width(2)
t.hideturtle()

length = 5
angle = 24

for i in range(300):
    # pick a random bright color
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor(r, g, b)
    
    t.forward(length)
    t.right(angle)
    
    # gradually increase segment length to open the spiral
    length += 2

turtle.done()
