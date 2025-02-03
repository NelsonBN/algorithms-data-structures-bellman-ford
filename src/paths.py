from collections import defaultdict


def bellman_ford(graph, origin):
    predecessors = defaultdict(lambda: (float('inf'), None))
    predecessors[origin] = (0, origin)

    # Relax edges V-1 times
    for _ in range(len(graph) -1):
        updated = False
        for departure, arrivals in graph.items():
            for arrival, cost in arrivals.items():
                current_distance, _ = predecessors[departure]
                new_accumulated_cost = current_distance + cost
                if new_accumulated_cost < predecessors[arrival][0]:
                    predecessors[arrival] = (new_accumulated_cost, departure)
                    updated = True
        if not updated:
            break

    # Check for negative cycles
    for departure, arrivals in graph.items():
        for arrival, cost in arrivals.items():
            current_distance, _ = predecessors[departure]
            new_accumulated_cost = current_distance + cost
            if new_accumulated_cost < predecessors[arrival][0]:
                raise Exception("Negative cycle detected")

    # Construct path
    paths = []

    for arrival, (_, predecessor) in predecessors.items():
        if arrival == origin:
            paths.append([origin])
        elif predecessor is None:
            continue
        else:
            path = [arrival]
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
