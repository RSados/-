n=int(input('enter: '))
sum1=0
sum2=0

for i in range(1,n+1):
    sum1+=i
    sum2+=i**2
sum1**=2

print(max(sum1,sum2)-min(sum1,sum2))
