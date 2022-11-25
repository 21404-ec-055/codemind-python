from math import*
def p(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
def pal(n):
    t=n
    rev=0
    while(n>0):
        k=n%10
        rev=(rev*10)+k
        n=n//10
    if(t==rev):
        return True
    else:
        return False
n=int(input())
n=n+1
while(True):
    if(pal(n)):
        if(p(n)==True):
            print(n)
            break
    n+=1