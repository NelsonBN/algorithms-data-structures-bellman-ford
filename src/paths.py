from collections import defaultdict


def bellman_ford(graph, origin):
    predecessors = defaultdict(lambda: (float('inf'), None))
    predecessors[origin] = (0, origin)

    # Relax edges V-1 times
    for _ in range(len(graph) -1):
        updated = False
        for node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                current_distance, _ = predecessors[node]
                accumulated_weight = current_distance + weight
                if accumulated_weight < predecessors[neighbor][0]:
                    predecessors[neighbor] = (accumulated_weight, node)
                    updated = True
        if not updated:
            break

    # Check for negative cycles
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            current_distance, _ = predecessors[node]
            accumulated_weight = current_distance + weight
            if accumulated_weight < predecessors[neighbor][0]:
                raise Exception("Negative cycle detected")

    # Construct path
    paths = []

    for neighbor, (_, predecessor) in predecessors.items():
        if neighbor == origin:
            paths.append([origin])
        elif predecessor is None:
            continue
        else:
            path = [neighbor]
            while predecessor != origin:
                path.insert(0, predecessor)
                _, predecessor = predecessors[predecessor]
            path.insert(0, origin)
            paths.append(path)

    return paths

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

paths = bellman_ford(graph, origin)
for path in paths:
    print(path)
