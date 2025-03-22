def alm(n):
    l=[]  
    def gen(c):
        if(c>1000):
            return
        if(c>0):
            l.append(c)
        gen(c*10+4)
        gen(c*10+7)   
    gen(0)
    for i in l:
        if(n%i==0):
            return "YES"
    return "NO"
n=int(input())
print(alm(n))