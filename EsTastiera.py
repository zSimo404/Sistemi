import turtle

robot = turtle.Turtle()
win = turtle.Screen()

def go():
    if((robot.xcor()+50<=400 and robot.xcor()-50>=-400) and(robot.ycor()+50<=400 and robot.ycor()-50>=-400)):
        robot.forward(50)
    else:
        robot.goto(0,0)

def left():
    robot.left(90)

def right():
    robot.right(90)


win.title("My game")
win.bgcolor("green")
win.setup(width=800, height=800)

win.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)
win.onkey(go, "w")
win.onkey(left, "a")
win.onkey(right, "d")

win.mainloop()