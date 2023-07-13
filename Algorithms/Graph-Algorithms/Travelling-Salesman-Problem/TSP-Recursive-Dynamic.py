# Working solution   - YES
# Solution Level     - Sub-Optimal
# Helping comments   - NO

def recur_sol(cities, costs, start, enter, visited):
    # Base case
    if len(cities)<=1:
        return costs[start][enter],[]
    
    # Startup Procedure
    each_cost = 0
    all_cost = []
    city_copy = cities.copy()
    city_copy.remove(start)
    path = []
    all_path = []
    res_path = [start]
    
    # Main logic
    for city in city_copy:
        path = []
        if not visited[city]:
            each_cost = 0
            path.extend([city])
            each_cost,next_city = recur_sol(city_copy,costs, city,enter,[False]*len(visited)) 
            path.extend(next_city)
            
        each_cost += costs[start][city]
        all_path.append(path)
        all_cost.append(each_cost)
        
    final_cost = min(all_cost)
    idx = all_cost.index(final_cost)
    final_path = all_path[idx]

    res_path.extend(final_path)
    if res_path[0] != enter:
        res_path.pop(0)
    else:
        res_path.append(enter)

    #print(all_path,'   ',res_path)
    return final_cost,res_path   
