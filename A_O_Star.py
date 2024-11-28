import heapq

class Node:
    def __init__(self, name, is_and_node, children=None, cost=0):
        self.name = name
        self.is_and_node = is_and_node
        self.children = children if children else []
        self.cost = cost
        self.best_cost = float('inf')
        self.best_parent = None

    def __str__(self):
        return f"Node(name={self.name}, is_and_node={self.is_and_node}, cost={self.cost}, best_cost={self.best_cost})"

def ao_star(start_node):
    open_list = []
    heapq.heappush(open_list, (start_node.cost, start_node))

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.best_cost <= current_node.cost:
            continue

        current_node.best_cost = current_node.cost

        if current_node.is_and_node:
            for child in current_node.children:
                if child.best_cost == float('inf'):
                    child.best_cost = child.cost
                    child.best_parent = current_node
                    heapq.heappush(open_list, (child.cost, child))
        else:
            if current_node.children:
                best_child = min(current_node.children, key=lambda child: child.best_cost)
                current_node.best_cost = best_child.best_cost + current_node.cost
                current_node.best_parent = best_child
                heapq.heappush(open_list, (current_node.best_cost, current_node))

    return current_node.best_cost

def main():
    nodeG = Node("G", False, cost=0)
    nodeF = Node("F", False, cost=0)
    nodeE = Node("E", False, cost=0)

    nodeD = Node("D", True, children=[nodeG, nodeF], cost=3)
    nodeC = Node("C", True, children=[nodeF, nodeE], cost=2)

    nodeB = Node("B", False, cost=0)
    nodeA = Node("A", True, children=[nodeB, nodeC, nodeD], cost=5)

    start_node = nodeA

    result = ao_star(start_node)

    print(f"Best cost to reach the goal node: {result}")

if __name__ == "__main__":
    main()
