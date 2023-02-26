import turtle

colors = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff", "#4b0082", "#8b00ff"]

window = turtle.Screen()
window.bgcolor("#000")
rainbow = turtle.Turtle()
rainbow.speed(0)
rainbow.width(5)

for i, color in enumerate(colors):
    rainbow.color(color)
    rainbow.penup()
    rainbow.goto(-200 + i*50, -200 + i*50)
    rainbow.pendown()
    rainbow.circle(200 - i*50)
    rainbow.penup()
    rainbow.goto(-150 + i*50, -150 + i*50)
    rainbow.pendown()
    rainbow.circle(150 - i*50)

rainbow.hideturtle()
window.exitonclick()
