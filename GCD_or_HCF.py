def compute_gcd(num1,num2):
    while(num2):
        num1,num2 = num2,num1%num2
    return num1
num1,num2=map(int,input().split())
num1=int(num1)
num2=int(num2)
print(compute_gcd(num1,num2))

n=int(input())
c=0
a=1
b=1
if n==0 or n==1:
    print("True")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("True")
    else:
        print("False")