def steps(i,n):
    if i==n:
        return 1
    if i>n:
        return 0
    s1=steps(i+1,n)
    s2=steps(i+2,n)
    return s1+s2
n=5
print(steps(0,n))
        
#memoization
def stepcache(i,n,cache):
    if i==n:
        return 1
    if i>n:
        return 0
    elif cache[i]!=-1:
        return cache[i]
    s1=stepcache(i+1,n,cache)
    s2=stepcache(i+2,n,cache)
    return s1+s2
cache=[-1]*(n+1)
print(stepcache(0,n,cache))
