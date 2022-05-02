def noo(n):
    x=0
    for i in range(1,n+1):
        num=i
        while num!=0:
            if num%10==1:
                x+=1
            num=num//10
    return(x) 

n=int(input('숫자를 입력해라: ',))
print(noo(n))