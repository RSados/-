list=[5,1,7,2,6,3]
def swap(i,j):
    a=list[i]
    list[i]=list[j]
    list[j]=a
i,j=3,5
swap(i,j)
print(list)