import turtle as t

n=30
t.color("purple")
t.begin_fill()
for x in range(n):
    t.forward(20)
    t.left(360/n)
t.end_fill()
