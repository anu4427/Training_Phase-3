def BFS(s,graph):
    q=[s]
    v=[s]
    while len(q)!=0:
        ele=q.pop(0)
        for i in graph[ele]:
            if i not in v:
                q.append(i)
                v.append(i)
    return v
graph={
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','E'],
    'D':['B','E'],
    'E':['C','D']
         }
print(BFS('C',graph))
    
