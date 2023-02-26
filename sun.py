import turtle

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("#87ceeb")

# Set up the turtle
sun = turtle.Turtle()
sun.speed(0)
sun.width(3)
sun.color("#ffdb58", "#ffdb58")

# Draw the sun
sun.begin_fill()
sun.circle(100)
sun.end_fill()

# Draw the sun rays
sun.color("#ffcc00", "#ffcc00")
sun.penup()
sun.goto(0, 150)
sun.pendown()
sun.begin_fill()
for _ in range(8):
    sun.forward(50)
    sun.backward(50)
    sun.right(45)
sun.end_fill()

# Hide the turtle
sun.hideturtle()

# Exit the window when clicked
window.exitonclick()
