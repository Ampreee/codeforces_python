n=int(input())
l=list(map(int,input().split()))
j=0
a=0
b=0
k=0
for i in range(n):
    if(l[i]%2==0):
        a+=1
        j=i+1
    else:
        b+=1
        k=i+1
if(a<b):
    print(j)
else:
    print(k)