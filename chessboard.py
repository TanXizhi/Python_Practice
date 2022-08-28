import turtle

t = turtle.Pen()
width = 30
t.speed(0)
for i in range(19):
    t.penup()
    t.goto(-230, -300+i*width)
    t.pendown()
    t.goto(-230+18*width, -300+i*width)

for i in range(19):
    t.penup()
    t.goto(-230+i*width, -300)
    t.pendown()
    t.goto(-230+i*width, -300+18*width)

turtle.done()
