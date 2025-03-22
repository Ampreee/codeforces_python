t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    min_rating=float('inf')
    rating_a = 0
    rating_b = 0
    for i in range(n):
        if a[i]==1:
            rating_a+=1
        elif a[i]==-1:
            rating_a-=1   
        if b[i]==1:
            rating_b+=1
        elif b[i]==-1:
            rating_b -= 1
    min_rating =abs(rating_a)-abs(rating_b)
    print(min_rating)