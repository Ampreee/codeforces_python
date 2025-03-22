import heapq
from collections import defaultdict
n,m = map(int,input().split())
l = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    l[u].append((v, w))
    l[v].append((u, w))
d=[float('inf')]*n
d[0]=0
m=[(0,0)]   
while(m):
    x,u=heapq.heappop(m)
    if(x>d[u]):
        continue
    for v, w in l[u]:
        if(d[u]+w < d[v]):
            d[v]=d[u]+w
            heapq.heappush(m,(d[v], v)) 
tot= 0
for i in range(1, n): 
    mi=float('inf')
    for u, w in l[i]:
        if(d[i]==d[u]+w):
            mi=min(mi,w)
    tot+= mi
print(tot)