def printLeftToRight(index, nums, n):
	if index == n:
		return 
 
	if index % 2 == 0:
		print(nums[index])
	printLeftToRight(index + 1, nums, n)
 
def printLeftToRightBetterOne(index, nums, n):
	if index >= n:
		return 
 
	print(nums[index])
	printLeftToRightBetterOne(index + 2, nums, n)
def printRightToLeftBetterOne(index, nums, n):
	if index >= n:
		return 
 
	printLeftToRightBetterOne(index + 2, nums, n)
	print(nums[index])
 
 
 
def printRightToLeftInReverseManner(index, nums, n):
	if index < 0:
		return 
	print(nums[index])
	printRightToLeftInReverseManner(index - 2, nums, n)

l=[1,2,3,4]
printLeftToRight(0, l, len(l))
printLeftToRightBetterOne(0, l, len(l))
printRightToLeftBetterOne(0, l, len(l))
n = len(l)
if n % 2 == 0:
	printRightToLeftInReverseManner(n - 2, l, n)
else:
	printRightToLeftInReverseManner(n - 1, l, n)
