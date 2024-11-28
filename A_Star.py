import heapq

def a_star(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (f_cost, node)
    g_costs = {node: float('inf') for node in graph}
    g_costs[start] = 0
    parents = {start: None}

    while priority_queue:
        current_f_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node].items():
            tentative_g_cost = g_costs[current_node] + weight
            if tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(priority_queue, (f_cost, neighbor))
                parents[neighbor] = current_node

    return g_costs, parents

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

    heuristic = {}
    h_nodes = input("Enter the nodes for which you want to specify heuristic values: ").split()
    for node in h_nodes:
        h_value = int(input(f"Heuristic for node {node}: "))
        heuristic[node] = h_value

    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    g_costs, parents = a_star(graph, start, goal, heuristic)
    path = reconstruct_path(parents, start, goal)

    print(f"Shortest path from {start} to {goal} using A*: {' -> '.join(path) if path else 'No path found'}")
    print(f"Total cost: {g_costs[goal] if g_costs[goal] != float('inf') else 'Unreachable'}")

main()
