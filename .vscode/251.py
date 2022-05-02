def printhello(n):
    print('hello')
    printhello(n-1) if n >1 else None
printhello(5)