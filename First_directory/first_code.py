import turtle

# Set the screen size
turtle.setup(width=500, height=500)

# Set the background color
turtle.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's color
t.color("white")

# Set the turtle's color again
t.color("red")

# Set the turtle's pen size
t.pensize(5)

# Start drawing the pattern
t.penup()
t.setposition(-200, -200)
t.pendown()

# Draw a circle
t.circle(100)

# Move the turtle to the next position
t.penup()
t.setposition(200, -200)
t.pendown()

# Draw a square
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# Move the turtle to the next position
t.penup()
t.setposition(0, 200)
t.pendown()

# Draw a triangle
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()