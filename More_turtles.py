import turtle


def drawsqr(a_turtle):
    i=0
    while i<4:
        a_turtle.forward(100)
        a_turtle.right(90)
        i=i+1


def drawart():
    window = turtle.Screen()
    window.bgcolor("black")
    
    bobby = turtle.Turtle()
    bobby.shape("turtle")
    bobby.color("white")

    i=0

    for i in range(1,37):
         drawsqr(bobby)
         bobby.right(10)

    window.exitonclick()
    
drawart()
