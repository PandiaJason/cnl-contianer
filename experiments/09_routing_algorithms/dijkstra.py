import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]
    while queue:
        curr_distance, curr_node = heapq.heappop(queue)

        for neighbor, weight in graph[curr_node].items():
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'A': 2, 'C': 1, 'D': 7},
        'C': {'A': 4, 'B': 1, 'D': 3},
        'D': {'B': 7, 'C': 3}
    }

    start_node = 'A'
    result = dijkstra(graph, start_node)
    print(f"Shortest paths from {start_node}:")
    for node, dist in result.items():
        print(f"{start_node} -> {node}: {dist}")
