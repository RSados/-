from dataclasses import asdict


a=input()
for i in range(0,len(a)+1):
    for q in range(0,i):
        print(a[q],end='')
    print()