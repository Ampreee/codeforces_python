s=input()
l=['h','e','l','l','o']
i=0
l1=[]
for j in s:
    if(j in l[i]):
        l1.append(j)
        i+=1
        if(i==len(l)):
            break
    else:
        continue
if(l==l1):
    print('YES')
else:
    print("NO")