n=int(input())
l=list(map(int,input().split()))
c1=c2=c3=c4=0
for i in l:
        if(i==1):
            c1+=1
        elif(i==2):
            c2+=1
        elif(i==3):
            c3+=1
        else:
            c4+=1
m=c4
p=min(c3,c1)
m+=p
c3-=p
c1-=p
m+=c3
m+=c2//2
if(c2%2):
    m+=1
    c1-=min(2,c1)
if c1>0:
    m+=(c1+3)//4
print(m)