import turtle

t=turtle.Pen()
t.shape('turtle')

for i in range(5):
    if i==0:
     n=20
    for l in range(4):
        t.forward(n)
        t.left(90)
    n+=20
    #함수를 이용하여도 가능