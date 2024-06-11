def keys(s,c=0):
    s=s.lower()
    sample=s[0]
    sample1=[]
    for i in range(len(s)):
        if s[i]!=sample:
            sample1.append(s[i])
    if sample!=sample1:
        c+=1
    return c
s='wWaAB'
print(keys(s))
