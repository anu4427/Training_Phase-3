# sum of elements in list
def num(i,l,n,s):
    if i<n:
        s+=l[i]
        i+=1
        num(i,l,n,s)
    else:
        print(s)
        return
l=[15,10,-5,81]
n=len(l)
i=0
s=0
num(i,l,n,s)
# Passing data from Parent function to child function
def printSum(index, n, nums, result):
    if index == n:
        print("Sum is:", result)
        return 
 
    result += nums[index]
    #result = result + nums[index]
    printSum(index + 1, n, nums, result)
 
# Passing data from child function to Parent function
def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)
    return nextElementsSum + nums[index]
result = printSum2(0, n, l)
print("Sum is:", result)
