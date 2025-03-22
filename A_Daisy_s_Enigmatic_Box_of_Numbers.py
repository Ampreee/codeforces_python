t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    l1=list(map(int,input().split()))
    l1=sorted(l1)
    a=s/2
    i=0
    for j in range(n):
        if(l1[j]>=a):
            i=j+1
            break
        i+=1
    if(n-i>=2):
        print("YES")
    else:
        print("NO")