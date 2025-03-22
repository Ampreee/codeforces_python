s=input()
l=[]
for i in range(len(s)):
    if(s[i].lower()=='a' or s[i].lower()=='e' or s[i].lower()=='i' or s[i].lower()=='o' or s[i].lower()=='u' or s[i].lower()=='y'):
        continue
    else:
        l.append('.')
        l.append(s[i].lower())
print(''.join(l))