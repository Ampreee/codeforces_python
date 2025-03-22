def lcs(a,b):
    m=float("-inf")
    for i in range(len(b)):
        j=0
        c=0
        x=i
        while(j<len(a) and x<len(b)):
            if(a[j] in b[x]):
                x+=1
                c+=1
            j+=1
        m=max(m,c)
    return m
t=int(input())
for _ in range(t):
    a = input()
    b = input()
    print(len(a)+len(b)-lcs(a,b))



