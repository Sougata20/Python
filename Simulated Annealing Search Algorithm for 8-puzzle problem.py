import random
import math

# Goal state of the puzzle
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Heuristic h1: Number of misplaced tiles
def h1(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                misplaced += 1
    return misplaced

# Heuristic h2: Manhattan distance
def h2(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = divmod(state[i][j] - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Get the position of the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

# Generate possible moves from the current state (neighbors)
def get_neighbors(state):
    x, y = find_blank(state)
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Swap blank with adjacent tile
            new_state = [row[:] for row in state]  # Copy the current state
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Simulated Annealing Algorithm
def simulated_annealing(state, heuristic, initial_temp=1000, cooling_rate=0.99, max_iterations=1000):
    current_state = state
    current_h = heuristic(state)
    temp = initial_temp
    
    for iteration in range(max_iterations):
        neighbors = get_neighbors(current_state)
        next_state = random.choice(neighbors)
        next_h = heuristic(next_state)
        
        # If the new state is better, move to it
        if next_h < current_h:
            current_state = next_state
            current_h = next_h
        else:
            # Accept the new state with a probability
            delta_h = next_h - current_h
            if random.random() < math.exp(-delta_h / temp):
                current_state = next_state
                current_h = next_h
        
        # Cool down
        temp *= cooling_rate
        
        # Stop if the goal state is reached
        if current_h == 0:
            return current_state, current_h
    
    return current_state, current_h

# Test the algorithm with a random start state
initial_state = [
    [1, 2, 3],
    [4, 8, 0],
    [7, 6, 5]
]

print("Initial state:")
for row in initial_state:
    print(row)

# Perform simulated annealing with both heuristics
print("\nUsing h1 (Number of misplaced tiles):")
solution_state, solution_h1 = simulated_annealing(initial_state, h1)
for row in solution_state:
    print(row)
print("Heuristic value:", solution_h1)

print("\nUsing h2 (Manhattan distance):")
solution_state, solution_h2 = simulated_annealing(initial_state, h2)
for row in solution_state:
    print(row)
print("Heuristic value:", solution_h2)
