def fun(n):
    a=0
    for i in range(1,n):
        a=i%5+a
    return a
n=8
print(fun(n))