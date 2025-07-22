def prim(graph, start):
    visited = set()
    mst = []
    total_cost = 0

    visited.add(start)

    while len(visited) < len(graph):
        min_edge = None
        min_weight = float('inf')

        for u in visited:
            for v, weight in graph[u]:
                if v not in visited and weight < min_weight:
                    min_edge = (u, v)
                    min_weight = weight

        if min_edge:
            u, v = min_edge
            visited.add(v)
            mst.append((u, v, min_weight))
            total_cost += min_weight

    return mst, total_cost

graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('D', 8), ('E', 5)],
    'C': [('B', 3), ('E', 7)],
    'D': [('A', 6), ('B', 8), ('E', 9)],
    'E': [('B', 5), ('C', 7), ('D', 9)]
}

mst, cost = prim(graph, 'A')
print("Minimum Spanning Tree edges:")
for u, v, w in mst:
    print(f"{u} - {v} = {w}")
print("Total cost of MST:", cost)
