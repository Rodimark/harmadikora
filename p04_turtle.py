import turtle
import random

def square():
    turtle.forward(100)
    turtle.goto(-50,50)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.pensize(5)

    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
def dobas():
    square()



def point(x,y):
    turtle.goto(x,y)
    turtle.dot(10, 'black')

window = turtle.Screen()

turtle.done()
turtle.onkey(dobas, "n")
turtle.onkey(turtle.bye, "d")
turtle.listen()
turtle.mainloop()