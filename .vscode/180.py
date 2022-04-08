a=int(input('숫자 입력: '))
b=0
for i in range(1,a+1):
    if int(a)%i==0:
        b+=1
if b==2:
    print('소수')
else:
    print('소수 아님')
print(b)