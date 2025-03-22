from collections import defaultdict
n, m, l = map(int, input().split())
l1=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    l1[a].append(b)
    l1[b].append(a)
c={}
tot=0
for i in range(n):
    count= 0
    x=l1[i+1]
    for k in range(len(x)):
        for j in range(k+1,len(x)):
            u=x[k]
            v=x[j]
            if(v in l1[u]):
                count+=1
    c[i+1]=count
    if(c[i+1]<l):
        tot+=1
print(tot)

