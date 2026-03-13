class Graph:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def kruskal(self, vertices):
        self.edges.sort()
        parent = {v: v for v in vertices}
        mst = []
        cost = 0

        for w, u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst.append((u, v, w))
                cost += w
                self.union(parent, x, y)

        print("Edges in MST:")
        for u, v, w in mst:
            print(u, "-", v, "=", w)

        print("Total cost:", cost)


g = Graph()

n = int(input("Enter number of edges: "))
vertices = set()

print("Enter u v weight")
for i in range(n):
    u, v, w = input().split()
    w = int(w)
    g.add_edge(u, v, w)
    vertices.add(u)
    vertices.add(v)

g.kruskal(vertices)