t=int(input())
for _ in range(t):
    n,k=map(int, input().split())    
    l1 = list(range(1,n+1)) 
    s=0 
    for i in range(1, n + 1):
        s+=abs(i-(n-i+1))
    if (k%2==1 or s<k):
        print("No")
    else:
        print("Yes")
        i=0
        j=n
        while (k>(j-1)*2):
            l1[i],l1[n-i-1]=l1[n-i-1],l1[i]
            k-=(j-1)*2
            j-=2
            i+=1
        k//=2
        l1[i],l1[i+k]=l1[i+k],l1[i]
        print(" ".join(map(str,l1)))


