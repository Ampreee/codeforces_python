t=int(input())
for _ in range(t):
    n=int(input().strip())
    s=input().strip()
    if(len(s)<=2):
        print(int(s))
    else:        
        m=float('inf')
        l=int(s[0:2])  
        c=2
        for i in range(len(s)-1):
            while(c<len(s)):
                if(c==i):
                    a=int(s[c:c+2])
                    c+=2
                else:
                    a=int(s[c])
                    c+=1
                if(l==1 or a==1 or l==0 or a==0):
                    l=a*l
                else:
                    l=a+l
            l=int(s[0])
            c=1
            m=min(m,l)
        print(m)