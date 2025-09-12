import turtle

# Correct way to set screen size and background color
screen = turtle.Screen()    # create a screen object
screen.bgcolor("orange")    # set background color
screen.setup(width=800, height=600)  # set screen size

# Create a turtle to draw
t = turtle.Turtle()
t.color("blue")

# Example: draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
