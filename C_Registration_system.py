t=int(input())
d={}
for _ in range(t):
    a=input()
    if(a not in d):
        d[a]=1
        print("OK")
    else:
        print(a+str(d[a]))
        d[a]+=1