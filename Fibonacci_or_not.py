def fib(n):
    a=0
    b=1
    while b<n:
        c=a+b
        a=b
        b=c
        if b==n or a==n:
            return True
        if b>n:
            return False
n=int(input())
if fib(n):
    print('True')
else:
    print('False')