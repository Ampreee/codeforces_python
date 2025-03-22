t = int(input())
for _ in range(t):
    n = int(input())
    a = (list(map(int, input().split())))
    b = (list(map(int, input().split())))
    if(sorted(a)!=sorted(b)):
        print("NO")
    else:
        p={value: idx for idx, value in enumerate(b)}
        n=len(a)
        c=0
        for i in range(n):
            if(a[i] != b[i]):
                c+=1
                s=p[a[i]]
                b[i], b[s]=b[s],b[i]
                p[b[s]] = s
                p[a[i]] = i
        if(c%2==0):
            print("YES")
        else:
            print("NO")


