import turtle
import random

turtle.screensize(canvwidth=500, canvheight=500)
turtle.speed("fastest")
turtle.hideturtle()
#turtle.bgcolor("black")
turtle.pensize(5)
turtle.penup()

#targetX = input("Target X: ")
#targetY = input("Target Y: ")
targetX = 200
targetY = 200
prevX = 0
prevY = 0

turtle.color("red")
turtle.setpos(int(targetX), int(targetY))
turtle.dot()

turtle.color("blue")

turtle.setpos(0,0)
turtle.dot()

turtle.color("black")

while (abs(turtle.xcor() - int(targetX)) > 25 or abs(turtle.ycor() - int(targetY)) > 25):
    turtle.pendown()
    angle = random.randint(0,361)
    distance = random.randint(0,100)

    prevX = turtle.xcor()
    prevY = turtle.ycor()

    turtle.setheading(angle)
    turtle.forward(distance)

    if(turtle.xcor() < -400 or turtle.xcor() > 400 or turtle.ycor() < -400 or turtle.ycor() > 400):
        turtle.color("white")
        turtle.setpos(prevX, prevY)
        turtle.color("black")

print("Found.")

turtle.done()
