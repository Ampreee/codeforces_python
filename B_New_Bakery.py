def max_profit(n, a, b):
        k=b-a+1
        k=min(k,n)
        if(k<0):
            k=0
        s=(n-k)*a  
        s+=((k*(2*b-k+1))//2)
        return s
t = int(input())
for _ in range(t):
    n,a,b=map(int, input().split())
    print(max_profit(n, a, b))
