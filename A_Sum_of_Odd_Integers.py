t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if(a<b*b):
        print("NO")
    elif(a%2!=b%2):
        print("YES")
    else:
        print("NO")