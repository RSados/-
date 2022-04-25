def gcd(n,m):
    a=0
    for i in range(1,m):#(m,1,-1)하면 m부터 1까지 1씩 감소
        if m%i==0:
            if n%i==0:
                if i>a:
                    a=i
    return a
def lcm(n,m):
    for i in range(1,n*m):
        if i%n==0:
            if i%m==0:
                return i
                break
n= int(input('1번째 숫자를 입력하세요: '))
m= int(input('2번째 숫자를 입려하세요: '))
print(n,'과',m,'의 최대 공약수는 ',gcd(n,m))
print(n,'과',m,'의 최소 공약수는 ',lcm(n,m))