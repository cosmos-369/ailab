#Python Implementation of DFS for Water Jug Problem
def water_jug_dfs(jug1_capacity, jug2_capacity, target):
    # Stack for DFS
    stack = [(0, 0)] # Initial state: both jugs are empty
    visited = set() # To keep track of visited states
    path = [] # To store the solution path
    # Helper function to perform DFS
    def dfs(jug1, jug2):
        # Check if we reached the target amount in either jug
        if jug1 == target or jug2 == target:
            path.append((jug1, jug2))
            return True
        # Mark the current state as visited
        visited.add((jug1, jug2))
        path.append((jug1, jug2))

        # Generate all possible moves
        possible_moves = [
        (jug1_capacity, jug2), # Fill jug1
        (jug1, jug2_capacity), # Fill jug2
        (0, jug2), # Empty jug1
        (jug1, 0), # Empty jug2
        (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug2 + jug1)), # Pour jug1 -> jug2
        (min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1))) # Pour jug2 -> jug1
        ]
        # Perform DFS for each move
        for new_jug1, new_jug2 in possible_moves:
            if (new_jug1, new_jug2) not in visited:
                if dfs(new_jug1, new_jug2):
                    return True
        # Backtrack if no solution is found in this path
        path.pop()
        return False
    
    # Start DFS
    dfs(0, 0)
    # Print solution path if target is reached
    if path and (path[-1][0] == target or path[-1][1] == target):
        print("Solution Path:")
        for state in path:
            print(f"Jug1: {state[0]}, Jug2: {state[1]}")
    else:
        print("No solution found")

# Example Usage
jug1_capacity = 4
jug2_capacity = 3
target = 2
water_jug_dfs(jug1_capacity, jug2_capacity, target)
