import turtle
import random

turtle.screensize(canvwidth=500, canvheight=500)

def main():
    value = 0
    turtle.setpos(0, 0)
    iteration = 1

    while True:
        targetX = random.randint(-400, 400)
        targetY = random.randint(-400, 400)
        value += find(targetX, targetY)
        print("Current Average: " + str(value / iteration) + " Iteration: " + str(iteration))
        iteration += 1
        turtle.reset()

    print("Average: " + str(value/100))

def find(targetX, targetY):
    turtle.speed("fastest")
    turtle.hideturtle()
    turtle.pensize(5)
    
    prevX = 0
    prevY = 0

    turtle.penup()
    turtle.color("red")
    turtle.setpos(int(targetX), int(targetY))
    turtle.dot()

    turtle.color("blue")

    turtle.setpos(0,0)
    turtle.dot()

    turtle.color("black")

    moves = 0

    while (abs(turtle.xcor() - int(targetX)) > 25 or abs(turtle.ycor() - int(targetY)) > 25):
        moves += 1
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
    
    return moves

main()

turtle.done()
