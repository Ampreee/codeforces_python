n, m = map(int, input().split())
l1=list(map(int,input().split()))
sum=[0]*(n+1)
for i in range(1,n+1):
    sum[i]=sum[i-1]+l1[i-1]
for i in range(m):
    a, b = map(int, input().split())
    a-=1
    l,r=a+1,n
    flag=True
    while(l<=r):
        mid=(l+r)//2
        if(sum[mid]-sum[a]>=b):
            flag=False
            r=mid-1
        else:
            l=mid+1
    if flag:
        print(-1)
    else:
        print(l)
