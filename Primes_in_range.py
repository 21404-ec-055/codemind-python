import math
n=10000001
seive=[True]*n
seive[0]=seive[1]=False
x=int(math.sqrt(n))
for i in range(1,x+1):
    if seive[i]:
        for j in range(i*i,n,i):
            seive[j]=False
start=int(input())
end=int(input())
c=0
for j in range(start,end+1):
    if seive[j]:
        c=c+1
print(c)