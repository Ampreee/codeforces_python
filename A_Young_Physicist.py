n=int(input())
l=[]
for i in range(n):
    l1=tuple(map(int,input().split()))
    l.append(l1)
s1=0
s2=0
s3=0
for i in l:
    x,y,z=i
    s1+=x
    s2+=y
    s3+=z
if(s1==0 and s2==0 and s3==0):
    print("YES")
else:
    print("NO")