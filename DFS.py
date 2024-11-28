from collections import defaultdict

def create_graph():
    graph = defaultdict(list)
    n = int(input("Enter the number of edges in the graph: "))
    print("Enter each edge as 'node1 node2':")
    for _ in range(n):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)
    return graph

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    traversal = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))

    return traversal

def main():
    graphs = []
    num_graphs = int(input("Enter the number of graphs: "))
    
    for i in range(num_graphs):
        print(f"\nCreating Graph {i+1}")
        graph = create_graph()
        graphs.append(graph)

    for i, graph in enumerate(graphs):
        print(f"\nGraph {i+1} structure: {dict(graph)}")
        start = input("Enter the start node for DFS: ")
        traversal = dfs(graph, start)
        print(f"DFS traversal from node {start}: {traversal}")

main()
