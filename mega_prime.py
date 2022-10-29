n=int(input())
inp=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        inp=False
        break
adp=True
while n>0:
    r=n%10
    if r!=2 and r!=3 and r!=5 and r!=7:
        adp=False
        break
    n=n//10
if inp and adp:
    print('Mega Prime')
else:
    print("Not Mega Prime")