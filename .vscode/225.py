array1=[[0]*4 for i in range(4)]
a=0
for i in range(4):
    for j in range(4):
     array1[i][j]=a
     a+=1
for i in range(4):
    print(array1[i])