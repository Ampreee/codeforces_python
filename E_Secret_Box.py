t=int(input())
for _ in range(t):
    x,y,z,k= map(int, input().split())
    m=0
    for i in range(1,x+1):
        for j in range(1,y+1):
            if(k%(i*j) == 0):
                v=k//(i*j)
                if(v<=z): 
                    l= (x-i+1)*(y-j+1)*(z-v+1)
                    m= max(m,l)
    print(m)