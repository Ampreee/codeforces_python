n,m=map(int,input().split())
l1=[]
l2=[]
for _ in range(m):
    a,b=map(int,input().split())
    l1.append(a)
    l2.append(b)
l={}
for i in range(m):
    l[l1[i]]=1
for i in range(m):
    l[l2[i]]+=1
print(sum(l.values()))