def gcd(i, j):
    if(j!=0):
        return gcd(j, i % j)
    else:
        return abs(i)

l1=list(map(int,input().split()))
l2=[]
for i in range(0,len(l1)-1):
    for j in range(i+1,len(l1)):
        l2.append(gcd(l1[i],l1[j]))

l1=l1+l2
print(min(l1))