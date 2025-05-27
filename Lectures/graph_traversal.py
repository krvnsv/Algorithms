def recursive_dfs(graph, start, path=[]):
    '''recursive depth first search from start'''
    path=path+[start]
    for node in graph[start]:
        if not node in path:
            path=recursive_dfs(graph, node, path)
    return path

def iterative_dfs(graph, start, path=[]):
    '''iterative depth first search from start'''
    q=[start]
    while q:
        v=q.pop(0)
        if v not in path:
            path=path+[v]
            q=graph[v]+q
    return path

def iterative_bfs(graph, start, path=[]):
    '''iterative breadth first search from start'''
    q=[start]
    while q:
        v=q.pop(0)
        if v not in path:
            path=path+[v]
            q=q+graph[v]
    return path



graph = {'S': ['A', 'B'], 
         'A': ['S', 'C'], 
         'B': ['S', 'C'], 
         'C':['A','B','E','D'],
         'D': ['C', 'E'],
         'E': ['D', 'C']}

print('recursive dfs ', recursive_dfs(graph, 'S'))
print ('iterative dfs ', iterative_dfs(graph, 'S'))
print ('iterative bfs ', iterative_bfs(graph, 'S'))
