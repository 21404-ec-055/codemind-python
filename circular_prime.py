n=int(input())
s=0
k=n
for i in range(1,n+1):
    if n%i==0:
        s=s+1
c=0
while(k!=0):
    r=k%10
    c=c*10+r
    k=k//10
b=0
for j in range(1,c+1):
    if c%j==0:
        b+=1
if(s==2 and b==2):
    print("circular prime")
elif(s==2 and b!=2):
    print("prime but not a circular prime")
elif(s!=2):
    print("not prime")