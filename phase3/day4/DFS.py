def DFS(s,graph,v=None):
    if v==None:
        v=[]
    v.append(s)
    for ne in graph[s]:
        if ne not in v:
            DFS(ne,graph,v)
    return v

graph={
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','E'],
    'D':['B','E'],
    'E':['C','D']
         }
print(DFS('C',graph))
