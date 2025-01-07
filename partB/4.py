class Node:
    def __init__(self, name, heuristic=0, is_and=False):
        self.name = name
        self.heuristic = heuristic
        self.children = []  # Corrected typo
        self.is_and = is_and
        self.optimal_path = []

    def add_child_group(self, group):
        """Adds a group of children to the node."""
        self.children.append(group)


def ao_star(node: Node):
    if not node.children:  # Base case: leaf node
        print(f"{node.name} is a leaf node with heuristic {node.heuristic}")
        return node.heuristic

    print(f"Evaluating node {node.name} with initial heuristic {node.heuristic}")
    costs = []
    paths = []

    # Evaluate each group of children
    for child_group in node.children:
        total_cost = 0
        group_path = []

        # Process each child in the group
        for child, cost in child_group:
            c = cost + ao_star(child)
            total_cost += c
            group_path.append((child, c))  # Store the actual child reference

        if node.is_and:
            print(f"AND Node {node.name}: adding costs of {[child.name for child, _ in group_path]} => total: {total_cost}")
        else:
            print(f"OR Node {node.name}: considering cost {total_cost} for child group {[child.name for child, _ in group_path]}")
        costs.append(total_cost)
        paths.append(group_path)

    # Choose the best path
    best_index = costs.index(min(costs))
    best_cost = costs[best_index]
    node.optimal_path = paths[best_index]

    print(f"Best cost for {node.name} is updated to {best_cost}")
    print(f"Optimal path: {[child.name for child, _ in node.optimal_path]}")
    node.heuristic = best_cost
    return best_cost


def print_optimal_path(node: Node, curr_path = []):
    curr_path.append(node.name)
    if not node.optimal_path:
        return curr_path

    for child, _ in node.optimal_path:
        print_optimal_path(child, curr_path)

    return curr_path


# Create nodes
a = Node('a')
b = Node('b')
c = Node('c', is_and=True)
d = Node('d', is_and=True)
e = Node('e', heuristic=7)
f = Node('f', heuristic=9)
g = Node('g', heuristic=3)
h = Node('h', heuristic=0)
i = Node('i', heuristic=0)
j = Node('j', heuristic=0)

# Define relationships
a.add_child_group([(b, 1)])
a.add_child_group([(c, 1), (d, 1)])

b.add_child_group([(e, 1)])
b.add_child_group([(f, 1)])

c.add_child_group([(g, 1)])
c.add_child_group([(h, 1), (i, 1)])

d.add_child_group([(j, 1)])

# Run AO* algorithm
print("Starting AO* algorithm")
optimal_cost = ao_star(a)
print("\nAO* algorithm completed.")
print(f"Optimal cost: {optimal_cost}")

# Print the optimal path
optimal_path = print_optimal_path(a)
print("\nOptimal path:")
print(" -> ".join(optimal_path))
