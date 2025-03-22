t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    l=[]
    while(n>m):
        l.append(n)
        n-=1
    for i in range(1,m+1):
        l.append(i)
    print(*l)