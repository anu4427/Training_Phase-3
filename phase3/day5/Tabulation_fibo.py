def findNthTermUsingTabulation(n):
    cache = [-1] * (n + 1)
    # Whatever base condition we wrote 
    # recursive solutin, we need to 
    # initialize them 
 
    cache[1] = 1 
    cache[2] = 1 
    # 1 - wherever 'n' is present, replace it with index 
    # 2 - wherever 'functionCall' is there replace it with cache 
 
    for index in range(3, n + 1):
        result1 = cache[index - 1]
        result2 = cache[index - 2]
        cache[index] = result1 + result2
 
    return cache[n]
n=int(input())
print(findNthTermUsingTabulation(n))
