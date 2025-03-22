t=int(input())
for _ in range(t):
    n=int(input())
    l1=list(map(int,input().split()))
    sum=0
    m=-1
    p=0
    for i in range(n):
        sum+=l1[i]
        m=max(m,l1[i])
        if(sum-m==m):
            p+=1
    print(p)
