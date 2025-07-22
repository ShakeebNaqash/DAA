def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(parent, u, v):
    u_root = find(parent, u)
    v_root = find(parent, v)
    parent[v_root] = u_root

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(len(vertices))]

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        u_idx = vertices.index(u)
        v_idx = vertices.index(v)
        if find(parent, u_idx) != find(parent, v_idx):
            union(parent, u_idx, v_idx)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 2),
    ('A', 'D', 6),
    ('B', 'C', 3),
    ('B', 'D', 8),
    ('B', 'E', 5),
    ('C', 'E', 7),
    ('D', 'E', 9)
]

mst, cost = kruskal(vertices, edges)
print("Minimum Spanning Tree edges:")
for u, v, w in mst:
    print(f"{u} - {v} = {w}")
print("Total cost of MST:", cost)
