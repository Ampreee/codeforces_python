s,n=map(int,input().split())
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    l.append([a,b])
l.sort()
flag=True
for i in range(n):
    if(s>l[i][0]):
        s+=l[i][1]
    else:
        print("NO")
        flag=False
        break
if(flag):
    print("YES")