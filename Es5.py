import turtle
import random 
import time

delay=0.1
score=0
high_score=0

win=turtle.Screen()
win.title("Snake")
win.bgcolor("green")
win.setup(width=600,height=600)
win.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("orange")
head.penup()
head.goto(0,0)
head.direction="Stop"

food=turtle.Turtle()
colors="red"
shapes="circle"
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

segments=[]
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score: 0  High score: 0",align="center",font=("arial",25,"italic"))

def goup():
    if head.direction!="down":
        head.direction="up"

def godown():
    if head.direction!="up":
        head.direction="down"

def goleft():
    if head.direction!="right":
        head.direction="left"

def goright():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

win.listen()
win.onkeypress(goup,"w")
win.onkeypress(godown,"s")
win.onkeypress(goleft,"a")
win.onkeypress(goright,"d")

while True:
    win.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="Stop"
        colors="red"
        shapes="square"
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score: {} High score: {}".format(score,high_score),align="center",font=("arial",25,"italic"))

    if head.distance(food)<20:
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        food.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        delay-=0.001
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {} High score: {}".format(score,high_score),align="center",font=("arial",25,"italic"))
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="Stop"
            colors="red"
            shapes="square"
            for segment in segments:
                segment.goto(1000,1000)
            segment.clear()

            score=0
            delay=0.1
            pen.clear()
            pen.write("Score: {} High score: {}".format(score,high_score),align="center",font=("arial",25,"italic"))
        time.sleep(delay)


win.mainloop()