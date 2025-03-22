def how(n,l,h,l1):
    while(l<h):
        m=(l+h)//2
        if(n<l1[m]): 
            h=m
        else: 
            l=m+1
    return l
m=int(input())
l1=sorted(list(map(int,input().split())))
q=int(input())
for _ in range(q):
    n=int(input())
    print(how(n,0,len(l1),l1))