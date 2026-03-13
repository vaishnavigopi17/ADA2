def topological_sort(n, edges):
    adj = [[0]*n for _ in range(n)]
    indegree = [0]*n
    for u, v in edges:
        adj[u][v] = 1
        indegree[v] += 1
    topo = []
    for _ in range(n):
        source = -1
        for i in range(n):
            if indegree[i] == 0:
                source = i
                break

        if source == -1:
            print("Topological sort not possible")
            return
        topo.append(source)
        indegree[source] = -1

        for j in range(n):
            if adj[source][j] == 1:
                indegree[j] -= 1

    print("Topological Order:", topo)
# Main
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v):")
for i in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

topological_sort(n, edges)