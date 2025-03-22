t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(input().strip())
    l1=[]
    for i in range(n):
        l1.append(input().strip())
    row1 = [[0]*(m+1) for _ in range(n)]
    row2= [[0]*(m+1) for _ in range(n)]
    for i in range(n):
        for j in range(1, m + 1):
            row1[i][j] = (int(l[i][j-1]) + row1[i][j-1]) % 3
            row2[i][j] = (int(l1[i][j-1]) + row2[i][j-1]) % 3
    col1= [[0]*(n+1) for _ in range(m)]
    col2 = [[0]*(n+1) for _ in range(m)]
    for j in range(m):
        for i in range(1,n+1):
            col1[j][i] = (int(l[i-1][j])+col1[j][i-1])%3
            col2[j][i] =(int(l1[i-1][j])+col2[j][i-1])%3
    flag=True
    for i in range(n):
        for j in range(m):
            if (row1[i][m]!=row2[i][m])or(col1[j][n]!=col2[j][n]):
                print("NO")
                flag=False
                break
        if(flag!=True):
            break
    if(flag):
            print("YES")
