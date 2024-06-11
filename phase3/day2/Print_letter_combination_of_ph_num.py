def printletter(word,index,r):
    d={
            '1':'',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
    if index == len(word):
        print(" ".join(r))
        return
    ch=word[index]
    for val in d[ch]:
        r.append(val)
        printletter(word,index+1,r)
        r.pop()

w='23'
printletter(w,0,[])
