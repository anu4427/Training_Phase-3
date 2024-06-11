def vowel(i,s,n,c):
    if i<n:
        if s[i] in 'aeiouAEIOU':
            c+=1
        vowel(i+1,s,n,c)
    else:
        print(c)
        return
s=input()
n=len(s)
vowel(0,s,n,0)
    
    
def vowels(i,s,n,c):
    if i==n:
        return c
    if s[i] in 'aeiouAEIOU':
        c+=1
    return vowel(i+1,s,n,c)
s1=input()
n1=len(s1)
vowels(0,s1,n1,0)
