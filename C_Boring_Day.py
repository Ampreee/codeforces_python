t=int(input())
for _ in range(t):
    n,l,r=map(int,input().split())
    l1=list(map(int,input().split()))
    c=0
    s=0
    i=0
    for j in range(n):
        s+=l1[j]
        while(s>r and i<=j):
            s-=l1[i]
            i+=1
        if(l<=s<=r):
            c+=1
            s=0
            i=j+1
    print(c)