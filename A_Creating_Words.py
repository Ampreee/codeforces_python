t=int(input())
for _ in range(t):
    s1,s2=map(str,input().split())
    temp=s1[0]
    s1=s2[0]+s1[1:]
    s2=temp+s2[1:]
    print(s1,s2)