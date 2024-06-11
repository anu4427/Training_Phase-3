def Binary_string(s,r,n):
    if s==n:
        print(r)
        return
    Binary_string(s+1,r+'1',n)
    Binary_string(s+1,r+'0',n)
n=4
Binary_string(0,'',n)
    
