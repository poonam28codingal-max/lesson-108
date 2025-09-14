import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")   # background color
screen.title("Turtle Star")

# Create a turtle
t = turtle.Turtle()
t.color("yellow")  # pen color
t.speed(3)         # drawing speed

# Draw a 5-pointed star
for _ in range(5):
    t.forward(100)    # length of star edge
    t.right(144)      # turn angle

# Finish
# draw
turtle.done()
