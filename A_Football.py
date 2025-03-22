n=int(input())
l={}
for i in range(n):
    a=input()
    if a in l:
        l[a]+=1
    else:
        l[a]=1
k=''
m=float("-inf")
for key in l:
    if(l[key]>m):
        m=l[key]
        k=key
print(k)