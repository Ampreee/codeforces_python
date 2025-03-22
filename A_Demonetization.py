n=int(input())
l1=list(map(int,input().split()))
flag=True
l1.sort()
for i in range(0,n-1):
    if(l1[i]==l1[i+1]):
        print("YES")
        flag=False
        break
if(flag):
    print("NO")