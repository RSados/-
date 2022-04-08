a=[1,2,3,4,5]
b=0
for i in range(1,6):
    for u in range(1,6):
         for y in range(1,6):
              for t in range(1,6):
                       for r in range(1,6):
                           if len({i,u,y,t,r,})==5:
                            b+=1
                            if b==50:
                              print(i,u,y,t,r) 