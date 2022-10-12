n=int(input())
sn=n*n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
rn=rev
srn=rn*rn
rev1=0
while srn>0:
    r=srn%10
    rev1=rev1*10+r
    srn=srn//10
print(rev1==sn)