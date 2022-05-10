n=input('숫자를 입력하세요: ').split(',')
m=[]
for i in range(len(n)):
    m+=[(int(n[i])%11)]

set=set(n)
print(len(set))