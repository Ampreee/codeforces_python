t=int(input())
for i in range (0,t):
    n=int(input())
    l1=list(map(int,input().split()))
    s=""
    if l1[n-1]-l1[0] !=0:
        print("YES")
        for i in range(0,n):
            if(i!=1):
                s+='R'
            else:
                s+='B'
        print(s)  
    else:
        print("NO")
