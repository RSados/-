def grade(n):
    if n<=100 and 90<n:
        return('a')
    elif n<=90 and 80<n:
        return('b')
    elif n<=80 and 70<n:
        return('c')
    elif n<=70 and 60<n:
        return('d')
    else:
        return('f')
n=int(input('성적을 입력하세요: '))
print(grade(n))