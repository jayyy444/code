# Function to check if the current color assignment is safe
def is_safe(node, graph, color, c):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, node):
    if node == len(graph):
        return True  #All vertices are assigned a color

    for c in range(1, m + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if graph_coloring_util(graph, m, color, node + 1):
                return True
            color[node] = 0  # Backtrack
    return False

# Main function to start graph coloring
def graph_coloring(graph, m):
    color = [0] * len(graph)
    if not graph_coloring_util(graph, m, color, 0):
        print("No solution exist with", m, "colors.")
        return
    
    print("Solution exists: Following are the assigned colors:")
    print(color)

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3  # Number of colors
graph_coloring(graph, m)
