def evennum(a,b):
    if a==b:
        None
    else:
        if a%2==0:
            print(a)
        else:
            None
        return evennum(a+1,b)

a=int(input('두 수를 입려해라'))
b=int(input('두 수를 입려해라'))
evennum(a,b)
