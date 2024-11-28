from collections import deque, defaultdict

def create_graph():
    graph = defaultdict(list)
    n = int(input("Enter the number of edges in the graph: "))
    print("Enter each edge as 'node1 node2':")
    for _ in range(n):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return result

def main():
    graphs = []
    num_graphs = int(input("Enter the number of graphs: "))
    
    for i in range(num_graphs):
        print(f"\nCreating Graph {i+1}")
        graph = create_graph()
        graphs.append(graph)

    for i, graph in enumerate(graphs):
        print(f"\nGraph {i+1} structure: {dict(graph)}")
        start = input("Enter the start node for BFS: ")
        traversal = bfs(graph, start)
        print(f"BFS traversal from node {start}: {traversal}")

main()
