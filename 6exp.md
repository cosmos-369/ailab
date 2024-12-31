This Python program solves the **Water Jug Problem** using a **Depth-First Search (DFS)** approach. The problem involves two jugs with specific capacities, and the goal is to measure an exact target amount of water using these jugs. Here’s a detailed explanation of the code:

---

### **Key Components and Logic**

1. **Inputs:**

   - `jug1_capacity`: Maximum capacity of Jug 1.
   - `jug2_capacity`: Maximum capacity of Jug 2.
   - `target`: The amount of water to measure.

2. **Data Structures:**

   - `stack`: This simulates the DFS, though it is initialized but not explicitly used within `dfs` since recursion handles traversal.
   - `visited`: A set to track visited states (`(jug1, jug2)`) and prevent revisiting them, avoiding infinite loops.
   - `path`: A list to store the sequence of states leading to the solution.

3. **Helper Function - `dfs(jug1, jug2)`**

   - Recursive function to explore all possible moves.
   - Base case:
     - If either `jug1` or `jug2` matches the `target`, the function appends the current state to the path and returns `True`.
   - Recursive steps:
     - Mark the current state `(jug1, jug2)` as visited.
     - Add the current state to the solution `path`.
     - Generate all possible moves (described below).
     - For each new state, recursively call `dfs`. If a solution is found, propagate `True` back up the recursive calls.
   - Backtracking:
     - If no solution is found from a state, remove it from `path` and return `False`.

4. **Possible Moves:**

   - `(jug1_capacity, jug2)`: Fill Jug 1 completely.
   - `(jug1, jug2_capacity)`: Fill Jug 2 completely.
   - `(0, jug2)`: Empty Jug 1 completely.
   - `(jug1, 0)`: Empty Jug 2 completely.
   - Pour water from Jug 1 to Jug 2:
     - `max(0, jug1 - (jug2_capacity - jug2))`: Water left in Jug 1 after pouring.
     - `min(jug2_capacity, jug2 + jug1)`: Water in Jug 2 after pouring.
   - Pour water from Jug 2 to Jug 1:
     - `min(jug1_capacity, jug1 + jug2)`: Water in Jug 1 after pouring.
     - `max(0, jug2 - (jug1_capacity - jug1))`: Water left in Jug 2 after pouring.

5. **Solution Check:**
   - After the DFS completes, the program checks if `path` contains the target state.
   - If so, it prints the solution path.
   - Otherwise, it reports that no solution exists.

---

### **Example Execution**

Input:

```python
jug1_capacity = 4
jug2_capacity = 3
target = 2
```

1. **Initialization:**

   - `stack = [(0, 0)]`
   - `visited = set()`
   - `path = []`

2. **DFS Steps:**

   - Start with `(0, 0)` (both jugs empty).
   - Explore moves:
     - Fill Jug 1: `(4, 0)`
     - Fill Jug 2: `(0, 3)`
     - Pour from Jug 1 to Jug 2, etc.
   - Recursively explore new states until `target` is found or all states are visited.

3. **Solution Path:**
   For `target = 2`, a valid path might be:
   ```
   Jug1: 0, Jug2: 0
   Jug1: 4, Jug2: 0
   Jug1: 1, Jug2: 3
   Jug1: 1, Jug2: 0
   Jug1: 0, Jug2: 1
   Jug1: 4, Jug2: 1
   Jug1: 2, Jug2: 3
   ```
   The program stops when `Jug1` or `Jug2` contains `2`.

---

### **Key Concepts Demonstrated**

1. **DFS:** The recursive exploration of all possible states.
2. **State Space Pruning:** The `visited` set ensures no duplicate exploration.
3. **Backtracking:** Removes unsuccessful paths to explore alternatives.
4. **Problem Representation:** Encodes the problem as a state space where states are `(jug1, jug2)`.

This approach ensures all possible configurations are explored efficiently to find the solution or determine that none exists.
