# define node class 
class Node: 
    def __init__(self, name, heuristic=0): 
        self.name = name 
        self.heuristic = heuristic
        self.children = [] 

    def add_child(self, name, type='OR'): 
        self.children.append((name, type)) 


def ao_star_search(node:Node, solution_path=[]): 

    # check if the current node is the last node 
    if not node.children: 
        return node.heuristic, solution_path + [node.name] 
    
    best_cost = float('inf') 
    best_path = None 

    for (child, ntype) in node.children: 
        if ntype == 'OR':
            # if node type(ntype) is or select the node with least cost 
            cost, path = ao_star_search(child, solution_path + [node.name])
            if cost < best_cost: 
                best_cost = cost 
                best_path = path 
        elif ntype == 'AND': 
            # and 
            tot_cost = 0 
            curr_path = solution_path + [node.name] 
            all_paths = [] 
            for child, _ in node.children: 
                cost, path = ao_star_search(child, curr_path)
                tot_cost += cost 
                all_paths.extend(path) 
            if tot_cost < best_cost: 
                best_cost = tot_cost 
                best_path = all_paths 

    return best_cost, best_path

# Define the nodes with heuristic values
A = Node("A", heuristic=5)
B = Node("B", heuristic=2)
C = Node("C", heuristic=4)
D = Node("D", heuristic=1)
E = Node("E", heuristic=3)

# Construct the graph with AND-OR relationships
A.add_child(B, "OR")
A.add_child(C, "OR")
B.add_child(D, "AND")
B.add_child(E, "AND")
C.add_child(D, "OR")

# Execute AO* from the start node
cost, path = ao_star_search(A)
print("Optimal Cost:", cost)
print("Solution Path:", " -> ".join(path))