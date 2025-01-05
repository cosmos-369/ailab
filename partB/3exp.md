Here's a detailed step-by-step explanation of the program:

---

### **1. Function Overview**

The `a_star_search` function implements the A\* search algorithm to find the shortest path in a graph from a `start` node to a `goal` node, using a heuristic function to guide the search.

---

### **2. Supporting Function: `reconstruct_path`**

This function backtracks from the `goal` node to the `start` node using the `came_from` dictionary, which stores the previous node for each node on the optimal path. It:

1. Starts at the `goal` node.
2. Traces back to the `start` node using `came_from`.
3. Reverses the collected path since it was built backwards.

---

### **3. Initialization**

#### **Priority Queue (`open_set`):**

A heap-based priority queue is initialized with the starting node:

```python
open_set = []
heapq.heappush(open_set, (0, start))
```

- The `heapq` ensures nodes are explored in the order of increasing \( f(x) \) (estimated total cost).
- Initially, only the `start` node is in the queue, with an \( f(x) \) of `0`.

#### **Tracking Paths (`came_from`):**

A dictionary is initialized to keep track of the previous node for each visited node:

```python
came_from = {}
```

#### **Cost Dictionaries (`g_score` and `f_score`):**

Two dictionaries are initialized:

- `g_score`: Actual cost from the `start` node to each node. All nodes are initialized to infinity (\( \infty \)) except `start`, which is 0.
- `f_score`: Estimated total cost (\( f(x) = g(x) + h(x) \)) for reaching the `goal` from each node. All nodes are initialized to infinity (\( \infty \)), except the `start`, which is initialized to its heuristic value.

```python
g_score = {node: float('inf') for node in graph}
g_score[start] = 0

f_score = {node: float('inf') for node in graph}
f_score[start] = heuristics[start]
```

---

### **4. Main Loop**

The algorithm iterates as long as the `open_set` (priority queue) is not empty.

#### **4.1. Extract the Node with the Lowest \( f(x) \):**

The node with the lowest \( f(x) \) is popped from the queue:

```python
_, curr = heapq.heappop(open_set)
```

#### **4.2. Goal Check:**

If the current node (`curr`) is the `goal`, the algorithm reconstructs and returns the path:

```python
if curr == goal:
    return reconstruct_path(came_from, curr)
```

#### **4.3. Explore Neighbors:**

For each neighbor of the current node, calculate a potential new path cost:

```python
for neighbour, cost in graph[curr]:
    g = g_score[curr] + cost
```

Here:

- `g_score[curr] + cost` is the new actual cost to reach `neighbour`.

#### **4.4. Update Costs if a Better Path is Found:**

If the new \( g(x) \) is lower than the previously recorded \( g(x) \) for the `neighbour`, update:

1. `came_from`: Record the current node as the predecessor of the neighbor.
2. `g_score`: Update the actual cost of the shortest path to the neighbor.
3. `f_score`: Update the estimated total cost (\( f(x) \)) for the neighbor.
4. Add the neighbor to the priority queue:

```python
if g < g_score[neighbour]:
    came_from[neighbour] = curr
    g_score[neighbour] = g
    f_score[neighbour] = g + heuristics[neighbour]
    heapq.heappush(open_set, (f_score[neighbour], neighbour))
```

---

### **5. Graph and Heuristics**

The `graph` and `heuristics` represent the problem:

#### **Graph:**

The graph is represented as a dictionary where each node maps to a list of tuples representing its neighbors and the cost to reach them:

```python
graph = {
    's': [('b', 4), ('c', 3)],
    'b': [('f', 5), ('e', 12)],
    'c': [('d', 7), ('e', 10)],
    'd': [('e', 2)],
    'e': [('g', 5)],
    'f': [('g', 16)],
    'g': [],
}
```

#### **Heuristics:**

The `heuristics` dictionary provides an estimate of the cost from each node to the goal:

```python
heuristics = {
    's': 14,
    'b': 12,
    'c': 11,
    'd': 6,
    'e': 4,
    'f': 11,
    'g': 0,
}
```

---

### **6. Running the Algorithm**

The algorithm starts at node `'s'` and searches for the shortest path to `'g'`. It uses the `graph` and `heuristics` to guide the search efficiently.

---

### **7. Output**

The final path is reconstructed and printed:

```python
for i in path:
    print(i, "->", end="")
```

For the given graph and heuristics, the shortest path from `'s'` to `'g'` is:

```
s -> c -> d -> e -> g ->
```

This is the result of balancing actual costs \( g(x) \) and estimated costs \( h(x) \) to efficiently find the optimal path.
