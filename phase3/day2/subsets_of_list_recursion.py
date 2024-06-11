""" complexity of the program is 2**n occurance """
def subset(i,l,n,r):
    if i==n:
        print(r)
        return
    r.append(l[i])
    subset(i+1,l,n,r)
    r.pop()# backtracking 
    subset(i+1,l,n,r)#subset(i+1,l,n,r+[l[i]])  
l=[10,20,30]
n=len(l)
subset(0,l,n,[])
