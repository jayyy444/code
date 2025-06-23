V = 4
INF = float('inf')
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

for k in range(V):
    for i in range(V):
        for j in range(V):
            if graph[i][k] + graph[k][j] < graph[i][j]:  
                graph[i][j] = graph[i][k] + graph[k][j]

print("The all pair shortest paths are")
r = 1
for row in graph:
    c = 1
    for val in row:
        print(f"from {r}->{c} the distance is: {val}")
        c += 1
    r += 1
    print("*"*30)
