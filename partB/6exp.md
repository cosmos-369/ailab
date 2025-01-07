### **Program Explanation**

This Python program solves the **Traveling Salesperson Problem (TSP)** using the **Nearest Neighbor Heuristic**, an approximate algorithm that provides a quick solution but not necessarily the optimal one. The TSP is a classic combinatorial optimization problem where the goal is to find the shortest possible route that visits every city once and returns to the starting city.

---

### **Key Concepts**

1. **Distance Matrix**:

   - The program uses a square matrix (`dist_matrix`) to represent distances between cities.
   - `dist_matrix[i][j]` gives the distance between city `i` and city `j`. A value of `0` on the diagonal means the distance from a city to itself is zero.

2. **Nearest Neighbor Heuristic**:

   - Starting from a specific city, always move to the nearest unvisited city.
   - Repeat until all cities are visited.
   - Finally, return to the starting city.

3. **Approximation**:
   - This heuristic does not guarantee the shortest route but is computationally efficient compared to exact solutions like dynamic programming or exhaustive search.

---

### **Function: `tsp_nearest_neighbor`**

#### **1. Input Parameters**

- `dist_matrix`: A 2D list representing the distance matrix.
- `start`: The index of the starting city (default is `0`).

#### **2. Variables and Initialization**

- `n`: The number of cities (length of the matrix).
- `unvisited`: A set of all cities except the starting city.
- `path`: A list to store the visited order of cities, initialized with the starting city.
- `current_city`: The city currently being visited (starts as the `start` city).
- `tot_cost`: The total distance traveled, initialized to `0`.

#### **3. Main Logic**

```python
while unvisited:
    next_city = min(unvisited,
                    key=lambda city: dist_matrix[current_city][city])
    tot_cost += dist_matrix[current_city][next_city]
    path.append(next_city)
    unvisited.remove(next_city)
    current_city = next_city
```

- While there are unvisited cities:
  1. Find the nearest unvisited city (`next_city`) using `min()`. The `key` parameter calculates the distance from the current city to each unvisited city.
  2. Update the total cost (`tot_cost`) by adding the distance from `current_city` to `next_city`.
  3. Add `next_city` to the path.
  4. Remove `next_city` from the `unvisited` set.
  5. Set `current_city` to `next_city`.

#### **4. Closing the Loop**

```python
tot_cost += dist_matrix[current_city][start]
path.append(start)
```

- Once all cities are visited, return to the starting city.
- Add the distance from the last visited city (`current_city`) back to the starting city (`start`) to `tot_cost`.
- Append the starting city to the `path` to complete the route.

#### **5. Output**

- `path`: The approximate route (order of cities visited).
- `tot_cost`: The total distance traveled.

---

### **Example Walkthrough**

#### **Distance Matrix**

```plaintext
   |  0   1   2   3
--------------------
 0 |  0  29  20  21
 1 | 29   0  15  17
 2 | 20  15   0  28
 3 | 21  17  28   0
```

- `dist_matrix[i][j]` represents the distance between city `i` and city `j`.

#### **Step-by-Step Execution**

1. **Initialization**:

   - `start = 0`
   - `unvisited = {1, 2, 3}`
   - `path = [0]`
   - `current_city = 0`
   - `tot_cost = 0`

2. **Iteration 1**:

   - Find the nearest city to `current_city = 0`:
     - Distances: `{1: 29, 2: 20, 3: 21}`
     - Nearest city: `2` (distance = 20).
   - Update:
     - `tot_cost = 20`
     - `path = [0, 2]`
     - `unvisited = {1, 3}`
     - `current_city = 2`

3. **Iteration 2**:

   - Find the nearest city to `current_city = 2`:
     - Distances: `{1: 15, 3: 28}`
     - Nearest city: `1` (distance = 15).
   - Update:
     - `tot_cost = 20 + 15 = 35`
     - `path = [0, 2, 1]`
     - `unvisited = {3}`
     - `current_city = 1`

4. **Iteration 3**:

   - Find the nearest city to `current_city = 1`:
     - Distances: `{3: 17}`
     - Nearest city: `3` (distance = 17).
   - Update:
     - `tot_cost = 35 + 17 = 52`
     - `path = [0, 2, 1, 3]`
     - `unvisited = {}`
     - `current_city = 3`

5. **Return to Start**:
   - Add the distance from `current_city = 3` to `start = 0`:
     - Distance = 21.
   - Final:
     - `tot_cost = 52 + 21 = 73`
     - `path = [0, 2, 1, 3, 0]`

#### **Output**

```plaintext
Approximate TSP Path: [0, 2, 1, 3, 0]
Total Distance: 73
```

---

### **Strengths of Nearest Neighbor Heuristic**

- **Simplicity**: Easy to implement and runs in \(O(n^2)\) time for \(n\) cities.
- **Speed**: Efficient for large datasets compared to exact algorithms like dynamic programming.

### **Limitations**

- **Suboptimal Solutions**: The heuristic often produces longer routes than the optimal one.
- **Greedy Nature**: Always choosing the nearest city can lead to poor global results.

For this example, the approximate path `[0, 2, 1, 3, 0]` is found with a total distance of 73. The actual optimal solution for small problems can be computed using exhaustive search or dynamic programming for comparison.
