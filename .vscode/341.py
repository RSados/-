def fun_1(n):
    num=1
    while n!=0:
        num*=n%10
        n//=10
    print(num)
    return num
n=846
while n>=10:
    n=fun_1(n)
print(n)