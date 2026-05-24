import heapq
import networkx as nx

G = nx.Graph()

edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'E', 3),
    ('E', 'D', 4),
    ('D', 'F', 11),
    ('E', 'F', 7),
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

def dijkstra(graph: nx.Graph, start: str):
    distances = {v: float('inf') for v in graph.nodes}
    distances[start] = 0
    predecessors = {v: None for v in graph.nodes}

    heap = [(0, start)]
    visited = set()

    while heap:
        current_dist, current = heapq.heappop(heap)

        if current in visited:
            continue
        visited.add(current)

        for _, new_v, new_weight in graph.edges(data='weight', nbunch=[current]):
            new_dist = current_dist + new_weight

            if new_dist < distances[new_v]:
                distances[new_v] = new_dist
                predecessors[new_v] = current
                heapq.heappush(heap, (new_dist, new_v))

    return distances, predecessors


def get_path(predecessors, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path if path[0] == start else []


start = 'A'
distances, predecessors = dijkstra(G, start)

print(f"Найкоротші шляхи від '{start}':\n")
print(f"{'До':>4} | {'Відстань':>9} | Шлях")
print("-" * 35)
for v in sorted(distances):
    if v == start:
        continue
    path = get_path(predecessors, start, v)
    print(f"{v:>4} | {distances[v]:>9} | {' → '.join(path)}")
