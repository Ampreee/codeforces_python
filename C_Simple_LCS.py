a=input()
b=input()
c=input()
d=input()
dp=[[[[0 for _ in range(len(d)+1)] for _ in range(len(c)+1)] for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        for k in range(1,len(c)+1):
            for l in range(1,len(d)+1):
                if(a[i-1]==b[j-1]==c[k-1]==d[l-1]):
                    dp[i][j][k][l]=dp[i-1][j-1][k-1][l-1]+1
                else:
                    dp[i][j][k][l] = max(dp[i-1][j][k][l],dp[i][j-1][k][l],dp[i][j][k-1][l],dp[i][j][k][l-1])
print(dp[len(a)][len(b)][len(c)][len(d)])
     
