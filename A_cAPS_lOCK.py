s=input()
flag=True
if(s.isupper()):
    print(s.lower())
else:
    for i in range(1,len(s)):
        if(s[i].islower()):
            flag=False
            break
    if(flag):
        l=[]
        if(s[0].isupper()):
            l.append(s[0])
        else:
            l.append(s[0].upper())
        for i in range(1,len(s)):
            l.append(s[i].lower())
        print(''.join(l))
    else:
        print(s)

