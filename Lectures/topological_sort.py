def iterative_topological_sort(graph, start,path=set()):
    q = [start]
    ans = []
    while q:
        v = q[-1]                   #item 1,just access, don't pop
        path = path.union({v})  
        children = [x for x in graph[v] if x not in path]    
        if not children:              #no child or all of them already visited
            ans = [v]+ans 
            q.pop()
        else: q.append(children[0])   #item 2, push just one child

    return ans

graph = {'S': ['A', 'B'], 
         'A': ['S', 'C'], 
         'B': ['S', 'C'], 
         'C':['A','B','E','D'],
         'D': ['C', 'E'],
         'E': ['D', 'C']}

print ('iterative topological sort ', iterative_topological_sort(graph, 'S'))
