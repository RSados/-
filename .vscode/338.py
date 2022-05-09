numbers= [12,23,48,42,32,50,72,34,19,71,60,40,94]
a=[]
for i in range(len(numbers)):
    a+=[numbers[i]%24]
set=set(a)
print(set)
print(len(set))
    