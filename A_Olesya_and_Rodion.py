n,t=map(int,input().split())
a=1
if(n==1)and(t==10):
    print(-1)
else:
    print(t,end='')
    if(t==10):
        a+=1
    for _ in range(a,n):
        print('0',end='')