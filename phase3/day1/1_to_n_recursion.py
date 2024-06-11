def Print(i,n):
    if i<=n:
        print(i)
        Print(i+1,n)#recursion
        #print(i)
    else:
        return
n=int(input())
Print(1,n)
