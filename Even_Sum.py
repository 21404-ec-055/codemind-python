n=int(input())
c=0
k=list(map(int,input().split()))
for i in k:
    if i%2==0:
        c+=i
print(c)