t=int(input())
for _ in range(t):
    l=sorted(list(map(int,input().split())))
    for i in range(5):
        l[0]+=1
        l.sort()
    print(l[0]*l[1]*l[2]) 