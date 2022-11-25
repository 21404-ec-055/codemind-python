def nextPalindrome(n):
    p=n+1
    temp=p
    rev=0
    while p>0:
        dig=p%10
        rev=rev*10+dig
        p=p//10
    if rev==temp:
        return temp
    return nextPalindrome(temp)
def prevPalindrome(n):
    p=n-1
    temp=p
    rev=0
    while p>0:
        dig=p%10
        rev=rev*10+dig
        p=p//10
    if rev==temp:
        return temp
    return prevPalindrome(temp)
n=int(input())
ne=nextPalindrome(n)
p=prevPalindrome(n)
d1=abs(n-ne)
d2=abs(n-p)
if d1==d2:
    print(p,ne)
elif d1>d2:
    print(p)
else:
    print(ne)