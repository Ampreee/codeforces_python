t=int(input())
for _ in range(t):
    x,y,k=map(int,input().split())
    while(k>0 and x!=1):
        a=min(k,y-(x%y))
        x+=a
        while(x%y==0):
            x//=y
        k-=a
    if(x==1):
        print(k%(y-1)+1)
    else:
        print(x+k)