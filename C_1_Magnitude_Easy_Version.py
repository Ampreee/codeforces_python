t = int(input())
for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))
    c1=[]
    c2=[]
    c1.append(f[0])
    c2.append (abs(f[0]))
    for i in range(1, n):
        c1.append(min(c1[i-1], c2[i-1]) + f[i]) 
        c2.append(max(abs(c1[i]), c2[i-1] + f[i]))
    print(max(c1[n-1],c2[n-1]))