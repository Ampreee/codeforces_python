def cut(l,l1,k):
    c=0
    for i in l1:
        c+=i//l
    return c>=k

n,k=map(int,input().split())
l1=[]
for i in range(n):
    l1.append(int(input()))
l=0
h=max(l1)
while (h-l > 1e-7):
    m=(l+h)/2
    if cut(m,l1,k):
        l=m
    else:
        h=m
print(l)