def fiboCache(n,cache):
    if n==0 or n==1:
        return n
    elif cache[n]!=-1:
        return cache[n]
    result1=fiboCache(n-1,cache)
    result2=fiboCache(n-2,cache)
    return result1+result2
n=int(input())
cache=[-1]*(n+1)
print(fiboCache(n,cache))
