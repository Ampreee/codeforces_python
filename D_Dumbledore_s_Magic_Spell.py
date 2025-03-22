n, m = map(int, input().split())
l1=list(map(int,input().split()))
num=0
for i in range(n):
    if(m%l1[i]==0):
        num+=1
print(num)