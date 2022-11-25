num=int(input())
sum=1
for i in range(2,num):
    if(num%i==0):
        sum=sum+i
if(sum>num): 
    print('True')
else:
    print('False')