# min element
def min(i,l,n,mi):
    if i<n:
        if mi>l[i]:
            mi=l[i]
        i+=1
        min(i,l,n,mi)
    else:
        print(mi)
        return
l=[15,10,-5,81]
n=len(l)
i=0
mi=l[0]
min(i,l,n,mi)

def print2(index, n, nums,m):
    if index < n:
        if m>nums[index]:
            m=l[index]
        return print2(index+1,n,nums,m)
    else:
        return m
m=l[0]
print(print2(i, n, l,m))
