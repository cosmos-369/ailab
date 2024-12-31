This Python program implements the **Breadth-First Search (BFS)** algorithm to solve the **8-puzzle problem**. The 8-puzzle is a sliding puzzle with a 3x3 grid containing numbers (1–8) and one empty space (`0`). The goal is to move the tiles into a specific target configuration.

---

### **Key Components and Logic**

1. **Inputs:**

   - `start`: The initial configuration of the puzzle (as a string).
   - `goal`: The desired configuration (as a string).

   For example:

   - `start = "123405678"`
   - `goal = "123456780"`

   The empty space (`0`) moves by sliding adjacent tiles.

2. **Class Definition:**
   - `Puzzle8BFS`: Encapsulates the BFS-based solver logic.

---

### **Steps in the Program**

#### **1. Initialization**

```python
self.start = start
self.goal = goal
self.visited = set()
```

- `self.start` is the initial configuration.
- `self.goal` is the target configuration.
- `self.visited` tracks explored states to avoid redundant computations and prevent infinite loops.

#### **2. Neighbor Generation (`get_neighbors`)**

This method generates all valid moves from the current state:

1. Converts the 1D string `state` into a 2D list `grid` for easier manipulation.
2. Finds the coordinates of the empty space (`0`) using `state.index('0')`.
3. Defines possible moves:
   - `"up"`, `"down"`, `"left"`, `"right"` using `(row, column)` offsets.
4. For each valid move:
   - Checks boundary conditions to ensure the new position is within the grid.
   - Swaps `0` with the adjacent tile.
   - Converts the updated 2D grid back to a string format for consistency.
5. Returns a list of neighbors as `(new_state, move)` pairs.

Example:

- For `state = "123405678"`, valid neighbors could be:
  - Move `down`: `"123450678"`
  - Move `right`: `"123045678"`

#### **3. Breadth-First Search (`bfs`)**

This method solves the puzzle using BFS:

1. Initializes a queue `deque([(self.start, [])])`:
   - Each element is a tuple: `(current_state, path_of_moves)`.
   - Starts with the initial configuration and an empty move path.
2. Marks `self.start` as visited.
3. Iteratively processes states from the queue:
   - Removes (`popleft`) the front state.
   - Checks if the current state matches the `goal`. If yes, returns the path of moves.
   - For each neighbor of the current state:
     - If it hasn't been visited, marks it as visited.
     - Adds the neighbor state and updated path to the queue.
4. If the queue is empty and no solution is found, returns `None`.

---

### **Example Execution**

#### **Input:**

```python
start_state = "123405678"
goal_state = "123456780"
```

#### **Execution Steps:**

1. **Initialization:**

   - `queue = deque([("123405678", [])])`
   - `visited = {"123405678"}`

2. **BFS Loop:**

   - Current state: `"123405678"`
   - Neighbors:
     - Move `down`: `"123450678"`
     - Move `right`: `"123045678"`
   - Queue after processing:
     - `deque([("123450678", ["down"]), ("123045678", ["right"])])`

3. Process each state in the queue:
   - Continue exploring until `goal_state = "123456780"` is reached.

#### **Output:**

```python
Solution found with BFS:
Step 1: Move down
Step 2: Move right
Step 3: Move up
Step 4: Move left
```

---

### **Key Concepts Demonstrated**

#### **Breadth-First Search (BFS):**

- Explores states level-by-level, ensuring the shortest solution is found first.
- Uses a queue to store states to be explored and avoids revisiting states with `visited`.

#### **State Representation:**

- Encodes the puzzle as a string for easier comparisons and manipulations.

#### **Neighbor Generation:**

- Dynamically calculates all valid moves from the current state based on the empty space's position.

#### **Optimality:**

- BFS guarantees the shortest sequence of moves to solve the puzzle, assuming all moves have equal cost.

---

### **Additional Notes**

1. **Time Complexity:**

   - BFS explores all possible states until the solution is found. For the 8-puzzle, the state space has \(9! = 362,880\) possible configurations, but pruning with `visited` significantly reduces unnecessary exploration.

2. **Space Complexity:**

   - BFS requires storing all visited states and the queue, which can grow large for complex puzzles.

3. **Improvements:**
   - Heuristic-based algorithms like **A\*** are often preferred for puzzles like this, as they combine BFS with heuristics for faster solutions.

This BFS implementation demonstrates a systematic and clear approach to solving the 8-puzzle problem.
