from collections import defaultdict,deque
def diameter(tree,n):

    def bfs(s):
        v=[False]*(n+1)
        q=deque([(s, 0)]) 
        v[s] = True
        m=0
        f=s
        while q:
            n2,di=q.popleft() 
            if (di>m):
                m=di
                f=n2
            for i in t[n2]:
                if not v[i]:
                    v[i]=True
                    q.append((i,di+1))      
        return f,m

    n1,_ = bfs(1)
    _,d= bfs(n1) 
    return d

n=int(input())
t=defaultdict(list)
for _ in range(n-1):
    j,k=map(int,input().strip().split())
    t[j].append(k)
    t[k].append(j)
e=n-1    
d=diameter(t, n)
m=(e-d)*2+d
print(m)