from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return order

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("BFS traversal:", bfs(graph, 'A'))