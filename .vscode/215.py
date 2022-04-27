def duvlr(n):
    a=tuple(n)
    b=set(a)  #리스트를 셋으로 변환하려하면 오류나 발생 듀플을 이용하여 변환할것
    if len(a)==len(b):
        print('ture')
    else:
        print('false')
    print(a,b)
n=(input('enter the number'))
duvlr(n)
