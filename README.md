# Algorithms and Data Structures - Bellman-Ford


## Characteristics
- Time complexity:
  - Best: O(V) (when there are no negative edges and the shortest path is found in the first iteration)
  - Average: O(V)
  - Worst: O(V x E)
  - Worst: O(V x E) (when all edges need to be relaxed in every iteration)
- Space complexity: O(V) (storing distances and predecessors)


## Graphs

### No negative cycles

```mermaid
graph LR
  A -->|4| B
  A -->|2| D
  B -->|2| C
  B -->|3| D
  B -->|3| E
  D -->|1| B
  D -->|6| C
  D -->|4| E
  E -->|-5| C
```

### With negative cycles

```mermaid
graph LR
  A -->|4| B
  A -->|2| D
  B -->|2| C
  B -->|3| D
  B -->|3| E
  C -->|4| D
  D -->|1| B
  D -->|4| E
  E -->|-9| C
```

## Demos

- [Distances](./src/distances.py)
- [Distances with improved](./src/distances_improved.py)
- [Paths](./src/paths.py)


## References
- [Other Algorithms & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
