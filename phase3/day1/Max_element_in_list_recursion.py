# max element
def max(i,l,n,m):
    if i<n:
        if m<l[i]:
            m=l[i]
        i+=1
        max(i,l,n,m)
    else:
        print(m)
        return
l=[15,10,-5,81]
n=len(l)
i=0
m=l[0]
max(i,l,n,m)

def print2(index, n, nums,ma):
    if index < n:
        if ma<nums[index]:
            ma=l[index]
        return print2(index+1,n,nums,ma)
    else:
        return ma
ma=l[0]
print(print2(i, n, l,ma))
