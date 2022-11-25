import math
n=10000001
seive=[True]*n
seive[0]=seive[1]=False
x=int(math.sqrt(n))
for i in range(x+1):
    if seive[i]:
        for j in range(i*i,n,i):
            seive[j]=False
s=int(input())
e=int(input())
for i in range(s,e+1):
    if seive[i]:
        print(i)