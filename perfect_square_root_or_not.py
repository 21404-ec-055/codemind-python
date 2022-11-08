import math
n=int(input())
x=math.sqrt(n)
if n-(int(x)**2)==0:
    print("True")
else:
    print("False")