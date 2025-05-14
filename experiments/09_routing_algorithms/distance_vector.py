def bellman_ford(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    return distance

if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 3, 'D': 2, 'E': 3},
        'C': {'B': 1, 'D': 4, 'E': 5},
        'D': {},
        'E': {'D': -5}
    }

    source = 'A'
    result = bellman_ford(graph, source)
    print(f"Distance vector from {source}:")
    for node, dist in result.items():
        print(f"{source} -> {node}: {dist}")
