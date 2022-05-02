import turtle

t=turtle.Pen()
t.shape('turtle')

for i in range(1):
    n=20
    for l in range(5):
        t.forward(n)
        t.left(90)
        t.forward(n)
        t.left(90)
        t.forward(n)
        t.left(90)
        t.forward(n)
        t.left(90)
        n+=20
    #함수를 이용하여도 가능