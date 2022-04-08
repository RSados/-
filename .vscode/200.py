a=0
for i in range(1,6):
    for u in range(1,6):
        if i!=u:
         for y in range(1,6):
             if i!=y and u!=y:
              for t in range(1,6):
                  if i!=t and u!=t and y!=t:
                       for r in range(1,6):
                           if i!=r and u!=r and y!=r and t!=r:
                            a+=1
                            if a==50:
                              print(i,u,y,t,r) 