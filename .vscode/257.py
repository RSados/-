def fibonacci(n):
    if n==1 or n==2:
        return 1
    else :
        a=fibonacci(n-1)+fibonacci(n-2)
        return a

n=int(input('숫자를 입력해라:'))
print(fibonacci(n))