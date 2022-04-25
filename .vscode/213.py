def sum(n):
    a=0
    if n>10:
      while n !=0:
        a+=n%10
        print('+',n%10,end='')
        n=(n-(n%10))//10
      print('=',a)
      if a>9:
       n=a
       a=0
       while n !=0:
        a+=n%10
        print('+',n%10,end='')
        n=(n-(n%10))//10
       print('=',a)
    return a
n=int(input('숫자를 입력하세요: '))
print(sum(n))
