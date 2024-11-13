# Use turtle graphics to make an infinite spiral
import turtle
x = 0
while x >= 0:
    speed = 300
    turtle.forward(x)
    turtle.right(90)
    x = x + 5

turtle.exitonclick()


