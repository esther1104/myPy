import turtle as t
import random

te=t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

ts=t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

def turn_right():
    t.setheading(0)

def turn_left():
    t.setheading(180)

def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

def play():
    t.forward(10)
    ang=te.towards(t.pos())
    te.setheading(ang)
    te.forward(9)
    if t.distance(ts)<12:
        star_x=random.randint(-230,230)
        star_y=random.randint(-230,230)
        ts.goto(star_x,star_y)
    if t.distance(te)>=12:
        t.ontimer(play,100)

t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()
play()
