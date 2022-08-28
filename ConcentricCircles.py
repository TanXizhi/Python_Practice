import turtle

t=turtle.Pen()
colors = ['red', 'green', 'purple', 'blue', 'orange']

t.speed(0)
t.width(4)

for i in range(100):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(colors[i%len(colors)])
    t.circle(20+i*10)

turtle.done()