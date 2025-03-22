n,m,k=map(int,input().split())
m=m-n
ans=1
i,j=k,k
while(m>0):
    m=m-(j-i+1)
    i=i-1
    j=j+1
    if(m >= 0):
        ans=ans+1
    if(j > n):
        j=n
    if(i < 1):
        i=1
    if((j-i+1)==n):
        ans=ans+(m//n)
        break
print(ans)