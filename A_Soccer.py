t=int(input())
for _ in range(t):
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    if(l1[0]>l1[1] and l2[0]>l2[1]):
        print("YES")
    elif(l2[1]>l2[0] and l1[1]>l1[0]):
        print("YES")
    else:
        print("NO")