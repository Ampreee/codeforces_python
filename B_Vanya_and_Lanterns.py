n,l=map(int,input().split())
l1=list(map(int,input().split()))
l1.sort()
d=2*max(l1[0],l-l1[n-1])
for i in range(n-1):
    d=max(d,l1[i+1]-l1[i])
print("{0:.10f}".format(d/2))