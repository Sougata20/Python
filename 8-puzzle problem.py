import heapq
import copy

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(value - 1, 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def misplaced_tiles(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                misplaced += 1
    return misplaced

def custom_heuristic(state):
    return misplaced_tiles(state) + manhattan_distance(state)

def is_goal(state):
    return state == goal_state

def generate_neighbors(state):
    neighbors = []
    zero_x, zero_y = [(ix, iy) for ix in range(3) for iy in range(3) if state[ix][iy] == 0][0]
    
    for dx, dy in DIRECTIONS:
        new_x, new_y = zero_x + dx, zero_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(state)
            new_state[zero_x][zero_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[zero_x][zero_y]
            neighbors.append(new_state)
    return neighbors

def a_star_search(start_state, heuristic_func):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic_func(start_state), 0, start_state, []))
    closed_set = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if tuple(map(tuple, state)) in closed_set:
            continue

        closed_set.add(tuple(map(tuple, state)))

        if is_goal(state):
            return path + [state]

        for neighbor in generate_neighbors(state):
            if tuple(map(tuple, neighbor)) not in closed_set:
                f_new = g + 1 + heuristic_func(neighbor)
                heapq.heappush(open_list, (f_new, g + 1, neighbor, path + [state]))

    return None

def main():
    start_state = []
    print("Enter the initial state (3x3 grid):")
    for i in range(3):
        row = list(map(int, input(f"Enter row {i+1} (space-separated): ").split()))
        start_state.append(row)

    print("\nSelect Heuristic Function:")
    print("1. h1(n) = 0")
    print("2. h2(n) = Number of misplaced tiles")
    print("3. h3(n) = Manhattan Distance")
    print("4. h4(n) = Custom Heuristic")
    choice = int(input("Enter the number (1-4) for the heuristic to use: "))

    if choice == 1:
        heuristic_func = lambda state: 0
    elif choice == 2:
        heuristic_func = misplaced_tiles
    elif choice == 3:
        heuristic_func = manhattan_distance
    elif choice == 4:
        heuristic_func = custom_heuristic
    else:
        print("Invalid choice. Exiting.")
        return

    solution = a_star_search(start_state, heuristic_func)

    if solution:
        print("\nSolution path:")
        for state in solution:
            for row in state:
                print(row)
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
