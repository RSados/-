import turtle
t=turtle.Pen()
t.color('blue')
t.pensize(5)
t.speed('slow')

for x in range(1,9):
    for j in range(10):
        if j % 2 == 0:
            t.up()
        else:
            t.down()
        t.forward(10)
    t.left(225)