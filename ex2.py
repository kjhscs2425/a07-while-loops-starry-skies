# make infinite circles, start with a small circle, then draw a bigger circle around it
import turtle
r = 15
turtle.teleport(0,0-(r+15/2))
while True:
    turtle.circle(r)
    r = r + 15
    turtle.teleport(0, 0 - (r+15/2))



turtle.exitonclick()

    


