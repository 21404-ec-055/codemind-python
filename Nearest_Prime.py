t=int(input())
for i in range(t):
    x=int(input())
    np=x
    while True:
        ip=True
        for j in range(2,int(np**0.5)+1):
            if np%j==0:
                ip=False
                break
        if ip==True:
            break
        np+=1
        
    pp=x
    while True:
        ip=True
        for j in range(2,int(np**0.5)+1):
            if pp%j==0:
                ip=False
                break
        if ip==True:
            break
        pp-=1
    if x-pp<=np-x:
        print(pp)
    else:
        print(np)