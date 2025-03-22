from collections import deque
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    s=input()
    flag=True
    v=[False]*(n+2)
    v[0]=True
    q=deque()
    q.append((0,0))
    v[0]=True
    while q:
        c,r= q.popleft()
        def jump():
            if(c==0 or s[c-1]=='L'):
                for j in range(1,m+1):
                    nc=c+j
                    if(nc==n+1):
                        return True
                    if ((nc<=n) and (s[nc-1]!='C') and not (v[nc])):
                        v[nc]=True
                        q.append((nc,r))
            return False
        def swim():
            if((c>0) and (c<=n) and (s[c-1]=='W') and (r<k)):
                nc=c+1
                if(nc==n+1):
                    return True
                if((nc<=n) and (s[nc-1]!='C') and not (v[nc])):
                    v[nc] = True
                    q.append((nc,r+1))
            return False
        if(jump()):
            print("YES")
            flag=False
            break
        elif(swim()):
            print("YES")
            flag=False
            break
    if(flag):
        print("NO")
    