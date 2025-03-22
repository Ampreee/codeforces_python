n=int(input())
l1=[]
for _ in range(n):
    a,b=map(int,input().split())
    l1.append([a,b])
l1.sort()
m=l1[n-1][1]/l1[n-1][0]
flag=True
for i in range(n-1):
    if(m<l1[i][1]/l1[i][0]):
        print("Happy Alex")
        flag=False
        break
if(flag):
    print("Poor Alex")
