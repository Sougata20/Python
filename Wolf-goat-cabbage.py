from collections import deque

def is_valid(state):
    """ Check if a given state is safe (no eating scenario). """
    F, W, G, C = state
    # Goat and wolf are together without the farmer if F != G and (G == W):
    if F != G and G == W:
        return 0
    # Goat and cabbage are together without the farmer if F != G and (G == C):
    if F != G and G == C:
        return 0
    return 1

def next_states(state):
    """ Generate all valid next states from the current state. """
    F, W, G, C = state
    next_states = []

    # Define moves: Farmer can move alone or with one item
    possible_moves = [
        (1 - F, W, G, C),  # Farmer alone
        (1 - F, 1 - W, G, C) if F == W else None,  # Farmer and Wolf
        (1 - F, W, 1 - G, C) if F == G else None,  # Farmer and Goat
        (1 - F, W, G, 1 - C) if F == C else None   # Farmer and Cabbage
    ]

    for move in possible_moves:
        if move and is_valid(move):
            next_states.append(move)
    return next_states

def solve_wgc():
    # Initial state: everything is on the left bank
    start = (0, 0, 0, 0)  # (F, W, G, C) - 0 for left bank, 1 for right bank
    goal = (1, 1, 1, 1)   # Goal state: everything on the right bank

    # Queue for BFS and set to track visited states
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        # Check if goal has been reached
        if current_state == goal:
            return path + [current_state]

        # Skip if this state is already visited
        if current_state in visited:
            continue

        visited.add(current_state)

        # Generate valid next states
        for next_state in next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))

    return None  # No solution found

# Running the solution
solution_path = solve_wgc()
if solution_path:
    print("Steps to solve the Wolf-Goat-Cabbage problem:")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")
