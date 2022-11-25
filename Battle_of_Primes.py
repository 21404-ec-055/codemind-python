from math import*
def isprime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
s=n+m
n1=s+1
while(True):
    if(isprime(n1)==True):
        a=n1
        break
    n1+=1
d=abs(a-s)
print(d)