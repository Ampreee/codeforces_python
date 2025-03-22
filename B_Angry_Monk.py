t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    m=max(l)
    s=sum(l)   
    s=s-m
    l.sort()
    for i in range(k-1):
        s+=l[i]-1          
    print(s)
    