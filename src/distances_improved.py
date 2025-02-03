from collections import defaultdict


def bellman_ford(graph, origin):
    distances = defaultdict(lambda: float('inf'))
    distances[origin] = 0

    # Traverse each node - iterations = number of nodes - 1
    for _ in range(len(graph) -1):
        updated = False
        for node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                accumulated_weight = distances[node] + weight
                if accumulated_weight < distances[neighbor]:
                    distances[neighbor] = accumulated_weight
                    updated = True
        if not updated:
            break

    # Check for negative cycles
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            accumulated_weight = distances[node] + weight
            if accumulated_weight < distances[neighbor]:
                raise Exception("Negative cycle detected")

    return distances

# No negative cycles
graph1 = {
    'A': { 'B': 4, 'D': 2 },
    'B': { 'C': 2, 'D': 3, 'E': 3 },
    'C': {},
    'D': { 'B': 1, 'C': 6, 'E': 4 },
    'E': { 'C': -5 },
}

# With negative cycles
graph2 = {
    'A': { 'B': 4, 'D': 2 },
    'B': { 'C': 2, 'D': 3, 'E': 3 },
    'C': { 'D': 4 },
    'D': { 'B': 1, 'E': 4 },
    'E': { 'C': -9 }
}

origin = 'A'
graph = graph1

distances = bellman_ford(graph, origin)
for key, value in distances.items():
    print(f"{origin} -> {key} ({value})")
