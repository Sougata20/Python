import heapq

def dijkstra(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (cost, node)
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    parents = {start: None}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return costs, parents

def reconstruct_path(parents, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path if path[0] == start else []

def main():
    graph = {}
    n = int(input("Enter the number of edges: "))
    print("Enter each edge as 'node1 node2 weight':")
    for _ in range(n):
        u, v, w = input().split()
        w = int(w)
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = w
        graph[v][u] = w  # Assuming an undirected graph; omit if directed

    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")
    
    costs, parents = dijkstra(graph, start, goal)
    path = reconstruct_path(parents, start, goal)

    print(f"Shortest path from {start} to {goal}: {' -> '.join(path) if path else 'No path found'}")
    print(f"Total cost: {costs[goal] if costs[goal] != float('inf') else 'Unreachable'}")

main()
