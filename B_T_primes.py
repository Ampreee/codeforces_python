import math
def soe(l):
    ip=[True]*(l+1)
    ip[0]=ip[1]=False
    for p in range(2,int(math.sqrt(l))+1):
        if ip[p]:
            for j in range(p*p,l+1,p):
                ip[j]=False
    pr= [p for p in range(2,l+1) if ip[p]]
    return pr
p=set(soe(10**6))
n=int(input())
l=list(map(int,input().split()))
for i in l:
    if(i<=0):
        print("NO")
    else:
        k=int(math.isqrt(i))
        if(k*k==i and k in p):
            print("YES")
        else:
            print("NO")