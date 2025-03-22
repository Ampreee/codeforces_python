t=int(input())
for _ in range(t):
    l1=list(map(int,input().split()))
    l1.sort()
    x=l1[1]
    print(abs(l1[0]-x)+abs(l1[1]-x)+abs(l1[2]-x))
