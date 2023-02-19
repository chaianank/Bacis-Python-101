import turtle

t = turtle.Pen()
t.shape("turtle")
t.pencolor("black")
t.fillcolor("red")
t.begin_fill()

for i in range(5):
    t.forward(100)
    t.right(144)

t.end_fill()
##t.hideturtle()
turtle.done()
