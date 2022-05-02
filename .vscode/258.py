def exp(a,n):
    b=a
    if n<=1:
        return a
    else:
        return a*exp(a,n-1)

a=int(input('숫자를 입력해라: '))
n=int(input('지수를 입력해라: '))
print(exp(a,n))