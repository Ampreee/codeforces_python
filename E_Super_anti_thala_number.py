a,b=map(int,input().split())
i=a+(9-a%9)
c=0
l1=[]
if('7' not in str(i)):
  l1.append(str(i))
  c+=1
k=2
z=1
while(z<=b):
    z=i*k
    if(z>b):
        break
    k+=1
    if('7' not in str(z)):
        l1.append(str(z))
        c+=1
for j in l1:
    for k in range(len(j)-1):
        if(j[k]==j[k+1]):
            c-=1
            break
print(c)
