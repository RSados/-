def asd(n,m):
    m28=[2]
    m30=[4,6,9,11]
    m31=[1,3,5,7,8,10,12]
    요일=['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    c=0
    for i in range(1,n):
        if i in m28:
            c+=28
        elif i in m30:
            c+=30
        else:
            c+=31
    c+=m
    print(요일[c%7-1])
n=int(input('x월? : '))
m=int(input('y월? : '))
asd(n,m)