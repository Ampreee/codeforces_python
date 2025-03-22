def find(x,e):
    if e[x]!=x:
        e[x]=find(e[x],e)
    return e[x]
a=input()
b=input()
c=input()
e={chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
for i,j in zip(a,b):
    x=find(i,e)
    y=find(j,e)
    if(x!=y):
        if(x<y):
            e[y]=x
        else:
            e[x]=y
result = [find(i,e) for i in c]
print(''.join(result))

