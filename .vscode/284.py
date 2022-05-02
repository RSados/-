import turtle

t=turtle.Pen()
t.shape('turtle')

def r(s):
    for i in range(1,5):
        t.forward(s)
        t.left(90)

def turtle_inf_squre(n):
    m=200
    for i in range(n):
        r(m)
        t.up()
        t.forward(m*0.1)
        t.left(90)
        t.forward(m*0.1)
        t.right(90)
        m=m*0.8
        t.down()
turtle_inf_squre(10)