from turtle import Turtle


def d(n):
    num=n
    while n!=0:
        num+=n%10
        n=n//10
    return num

def isSelfnum(n):
    booleab=True
    for i in range(1,n):
        if n==d(i):
            boolean=False
    return boolean

n=int(input('숫자 입력해라: '))
print(isSelfnum(n))