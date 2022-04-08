a=10
b=1
for i in range(0,11):
    for l in range(0,a):
        print(' ',end='')
    for r in range(0,b):
        print('*',end='')
    b+=2
    a-=1
    print()