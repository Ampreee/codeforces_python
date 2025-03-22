t=int(input())
for _ in range (t):
    n=int(input())
    l1=list(map(int,input().split()))
    max=-1
    n=len(l1)
    for i in range(n-1):
        if(l1[i]>max):
            max=l1[i]
    print(l1[n-1]+max)