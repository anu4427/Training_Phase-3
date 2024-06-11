# Child function to parent function
def findSum(index, nums, n):
	if index == n:
		return 0 
	nextEleSum = findSum(index + 1, nums, n)
	if nums[index] % 5 == 0:
		nextEleSum += nums[index] 
	return nextEleSum
 
# parent function to child function 
def findSum2(index, nums, n, result):
	if index == n:
		print("Sum is:", result)
		return 
	if nums[index] % 5 == 0:
		result += nums[index]
	findSum2(index + 1, nums, n, result)
l=[1,2,3,40,51,6,4,5]
print(findSum(0,l,len(l)))
findSum2(0,l,len(l),0)
