def printThis(i,n):
    if i>=n:
        print("Base condition got hit")
        return
    print("Ending Line",i)
    for j in range(1,i):
        print(j)
    printThis(i+1,n)
    print("Starting Line",i)
printThis(1,8)
