t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=[list(map(int,input().split())) for _ in range(n)]      
    for i in range(n):
        for j in range(m):
            flag=True
            a=float('-inf')
            if i > 0 :
                if(l[i-1][j] < l[i][j]):
                    a=max(a,l[i-1][j])
                else:
                    flag=False
            if i < n-1:
                if(l[i+1][j] < l[i][j]):
                    a=max(a,l[i+1][j])
                else:
                    flag=False
            if j > 0 :
                if(l[i][j-1] < l[i][j]):
                    a=max(a,l[i][j-1])
                else:
                    flag=False
            if j < m-1:
                if(l[i][j+1] < l[i][j]):
                    a=max(a,l[i][j+1])
                else:
                    flag=False

            if(flag and a!=float('-inf')):
                l[i][j]=a
    for i in range(n):
        print(*l[i])

    