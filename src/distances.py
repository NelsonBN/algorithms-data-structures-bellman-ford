from collections import defaultdict


def bellman_ford(graph, origin):
    distance = defaultdict(lambda: float('inf'))
    distance[origin] = 0

    # Traverse each node - iterations = number of nodes - 1
    for _ in range(len(graph) -1):
        for departure, arrivals in graph.items():
            for arrival, cost in arrivals.items():
                new_accumulated_cost = distance[departure] + cost
                if new_accumulated_cost < distance[arrival]:
                    distance[arrival] = new_accumulated_cost

    # Check for negative cycles
    for departure, arrivals in graph.items():
        for arrival, cost in arrivals.items():
            new_accumulated_cost = distance[departure] + cost
            if new_accumulated_cost < distance[arrival]:
                raise Exception("Negative cycle detected")

    return distance

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
graph = graph2

result = bellman_ford(graph, origin)
for key, value in result.items():
    print(f"{origin} -> {key} ({value})")
