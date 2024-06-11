def printValidOnes(r,n,c1,c2):
    if c2>c1:
        return
    if c1>n//2 or c2>n//2:
        return
    if len(r)==n:
        print(r)
        return
    printValidOnes(r+'(',n,c1+1,c2)
    printValidOnes(r+')',n,c1,c2+1)

n=int(input())
if n%2==1:
    print("Invalid")
    exit(0)
printValidOnes('',n,0,0)
