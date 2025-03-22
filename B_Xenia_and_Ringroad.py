n,m=map(int,input().split())
l=list(map(int,input().split()))
x=l[0]-1
for i in range(1,len(l)):
    if(l[i]<l[i-1]):
        x+=(n-l[i-1])+l[i]
    else:
        x+=(l[i]-l[i-1])
print(x)