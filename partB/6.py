def tsp_nearest_neighbor(dist_matrix, start=0): 

    n = len(dist_matrix) 
    unvisited = set(range(n))
    unvisited.remove(start) 
    path = [start] 

    current_city = start 
    tot_cost = 0 

    while unvisited: 
        next_city = min(unvisited, 
                        key=lambda city: dist_matrix[current_city][city])
        tot_cost += dist_matrix[current_city][next_city] 
        path.append(next_city) 
        unvisited.remove(next_city) 
        current_city = next_city 
    
    tot_cost += dist_matrix[current_city][start]
    path.append(start) 

    return path, tot_cost 

dist_matrix = [
 [0, 29, 20, 21],
 [29, 0, 15, 17],
 [20, 15, 0, 28],
 [21, 17, 28, 0]
]

start_city = 0
path, total_cost = tsp_nearest_neighbor(dist_matrix, start=start_city)
print("Approximate TSP Path:", path)
print("Total Distance:", total_cost)
