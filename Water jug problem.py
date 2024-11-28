from collections import deque

def water_jug_bfs():
    start = (0, 0)  # Initial state: both jugs are empty
    goal = 2  # We want exactly 2 liters in either jug

    queue = deque([(start, [])])  # Queue to store the states to explore, with each step's path
    visited = set()  # Set to track visited states

    while queue:
        (x, y), path = queue.popleft()

        # Check if we've reached the goal
        if x == goal or y == goal:
            return path + [(x, y)]

        # Skip if this state has already been visited
        if (x, y) in visited:
            continue

        visited.add((x, y))  # Mark the state as visited

        # Generate possible moves from the current state
        possible_moves = [
            (4, y),  # Fill Jug X
            (x, 3),  # Fill Jug Y
            (0, y),  # Empty Jug X
            (x, 0),  # Empty Jug Y
            (min(x + y, 4), y - (min(x + y, 4) - x)) if x + y > 4 else (x + y, 0),  # Pour Y into X
            (x - (min(x + y, 3) - y), min(x + y, 3)) if x + y > 3 else (0, x + y)  # Pour X into Y
        ]

        # Enqueue new states with the updated path
        for move in possible_moves:
            if move not in visited:
                queue.append((move, path + [(x, y)]))

    return None  # No solution found

# Running the BFS to solve the water jug problem
solution_path = water_jug_bfs()
if solution_path:
    print("Steps to measure 2 liters:")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")
