import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Square inside Square")

# Create a turtle
t = turtle.Turtle()
t.color("darkred")
t.speed(3)   # drawing speed
t.pensize(2)

# Number of squares
num_squares = 5
size = 50     # starting size of the smallest square

for _ in range(num_squares):
    # Draw a square
    for _ in range(4):
        t.forward(size)
        t.right(90)
    # Move turtle to start next square
    t.penup()
    t.goto(t.xcor() - 10, t.ycor() + 10)  # adjust position for next square
    t.pendown()
    size += 20   # increase size for next square

# Finish
turtle.done()
