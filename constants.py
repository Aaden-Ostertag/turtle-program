import turtle

t = turtle.Turtle()
screen = t.getscreen()
canvas = screen.getcanvas()
root = canvas.master

t.hideturtle()
t.speed("fastest")
screen.bgcolor('grey')
t.pensize(15)
t.pencolor('red')