import heapq 

def a_star_search(graph, start, goal, heuristics): 

    def reconstruct_path(came_from, curr): 
        total_path = [curr] 
        while curr in came_from: 
            curr = came_from[curr] 
            total_path.append(curr) 
        total_path.reverse() 
        return total_path

    # push the start node to the list 
    open_set = [] 
    heapq.heappush(open_set, (0, start))

    # crete a dict to keep track of the previous node  
    came_from = {} 

    # initialize dict's to store g(x) and f(x) 
    g_score = {node:float('inf') for node in graph} 
    g_score[start] = 0 
    f_score = {node:float('inf') for node in graph} 
    f_score[start] = heuristics[start]

    # there are still nodes left in the priority queue 
    while open_set: 
        _, curr = heapq.heappop(open_set) 
        if curr == goal: 
            return reconstruct_path(came_from, curr) 

        for neighbour, cost in graph[curr]: 
            g = g_score[curr] + cost 
            if g < g_score[neighbour]: 
                came_from[neighbour] = curr 
                g_score[neighbour] = g 
                f_score[neighbour] = g_score[neighbour] + heuristics[neighbour] 
                heapq.heappush(open_set, (f_score[neighbour], neighbour)) 

graph = {
    's' : [('b', 4), ('c', 3)],
    'b' : [('f', 5), ('e', 12)],
    'c' : [('d', 7), ('e',10)], 
    'd' : [('e', 2)], 
    'e' : [('g', 5)], 
    'f' : [('g', 16)], 
    'g' : [],
}

heuristics = {
    's' : 14, 
    'b' : 12, 
    'c' : 11, 
    'd' : 6, 
    'e' : 4, 
    'f' : 11, 
    'g' : 0,
}

start = 's'
goal = 'g'

path = a_star_search(graph, start, goal, heuristics) 
for i in path: 
    print(i, "->", end="")