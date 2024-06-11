def printThis(pos):
    print("Leaving here",pos)
    if pos==0:
        print("Base condition got hit")
        return
    if pos%2==1:
        print("Even position:",pos)
    else:
        print("Odd position:",pos)
    printThis(pos-1)
    for i in range(pos,-1,-1):
        print("Index is:",i)
    print("Entering here",pos)
printThis(11)
