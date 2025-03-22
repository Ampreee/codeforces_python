t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=input()
    l1=sorted(set(map(int, input().split())))
    b=sorted(input())
    l2=list(a)
    for i in range(len(l1)):
        l2[l1[i]-1] = b[i]
    print(''.join(l2))