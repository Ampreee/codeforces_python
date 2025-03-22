
t = int(input())  
for _ in range(t):
    n, m = map(int, input().split())
    l1 = []
    for i in range(n):
        r = list(input().strip())
        l1.append(r)
    mi1,ma1=n,-1
    mi2,ma2=m,-1
    for i in range(n):
        for j in range(m):
            if(l1[i][j]=='#'):
                if(i<mi1):
                    mi1 = i
                if(i>ma1):
                    ma1=i
                if(j<mi2):
                    mi2=j
                if(j>ma2):
                    ma2=j
    x=((mi1+ma1)//2)+1  
    y=((mi2+ma2)//2)+1
    print(x,y)
