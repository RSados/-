def countdown(n):
    if n==0:
        print('- 끝 -')
    else:
        print(n,'남았습니다!')
        return countdown(n-1)

n=int(input('숫자를 입력하세요: '))
countdown(n)