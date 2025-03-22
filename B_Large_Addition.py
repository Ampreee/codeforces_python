t=int(input())
for i in range (0,t):
    n=int(input())
    if(n<10):
        print("NO")
    l1=[]
    while(n>0):
        l1.append(n%10)
        n//=10
    flag=True
    for i in range(1, len(l1)):
        if i == len(l1) - 1:
            k = l1[i] * 10 + l1[i - 1]
        else:
            k = 10 + l1[i - 1]

        if 10 <= k and k <= 18:
            l1[i] -= 1
        else:
            print("NO")
            flag=False
            break
    if(flag):
        print("YES")