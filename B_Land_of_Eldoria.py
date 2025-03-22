from collections import defaultdict
def find(x, p):
    if p[x]!=x:
        p[x]=find(p[x], p)
    return p[x]
def union(a,b,p,r):
    y=find(a,p)
    x=find(b,p)
    if(x!=y):
        if(r[x]>r[y]):
            p[y]=x
        elif(r[x]<r[y]):
            p[x]=y
        else:
            p[y]=x
            r[x]+= 1
n = int(input())
edges=[]
for _ in range(n - 1):
    a,b=map(int,input().split())
    edges.append([a,b])
p = list(range(n+1))  
r = [0]*(n + 1) 
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
    union(a, b, p, r)
c=defaultdict(list)
for node in range(1, n + 1):
    root = find(node,p)
    c[root].append(node)
rem=[]
cr=list(c.keys())
for i in range(len(cr)-1):
    root1=cr[i]
    root2=cr[i+1]
    node1=c[root1][0]
    node2=c[root2][0]
    graph[node1].append(node2)
    graph[node2].append(node1)
    union(node1,node2,p,r)
    rem.append((edges[i][0],edges[i][1],node1,node2))
print(len(rem))
for i in rem:
    print(*i)
