import networkx as nx
import matplotlib.pyplot as plt
 
# Step 3: Define the graph
graph = {'S': ['A', 'B'], 'A': ['S', 'C'], 'B': ['S', 'C'], 'C': ['A', 'B', 'E', 'D'], 'D': ['C', 'E'], 'E': ['D', 'C']}
 
# Step 4: Create a graph object
G = nx.Graph(graph)
 
# Step 5: Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=2000, node_color='lightblue', font_size=15, font_weight='bold', edge_color='gray')
plt.title('Graph Visualization')
plt.show()

def iterative_bfs(graph, start, visited):
    '''Iterative breadth-first search from start, returns all reachable nodes from start'''
    q = [start]
    component = []
    while q:
        v = q.pop(0)
        if v not in visited:
            visited.add(v)
            component.append(v)
            q.extend(graph[v])
    return component
 
def count_connected_components(graph):
    '''Count the number of connected components in an undirected graph'''
    visited = set()  # Set to track visited nodes
    components = []  # List to hold the components
 
    for node in graph:
        if node not in visited:
            component = iterative_bfs(graph, node, visited)
            components.append(component)  # Add the component to the list
 
    return len(components), components
 
# Test with your graph
graph = {
    'S': ['A', 'B'], 
    'A': ['S', 'C'], 
    'B': ['S', 'C'], 
    'C': ['A', 'B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C']
}
 
# Call the function to find the number of connected components
num_components, components = count_connected_components(graph)
 
# Output results
print(f'Number of connected components: {num_components}')
print(f'Connected components: {components}')