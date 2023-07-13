# Working solution   - YES
# Solution Level     - Optimal(Can be refractored,there are so many variables used.)
# Helping comments   - YES

def recur_sol(cities, costs, start, enter, visited):
    # Base case
    if len(cities)<=1:
        return costs[start][enter],[]
    
    # Startup Procedure
    each_cost = 0
    all_cost = []
    
    # Duplicating the cities list, to avoid memory overlap in lists.
    city_copy = cities[:]
    city_copy.remove(start)
    
    path = []
    all_path = []
    result_path = [start]
    
    # Main logic
    # Scroll down to get help on <Tags>.
    for city in city_copy:
        path = []
        next_city = []
        
        #Tag-1
        if not visited[city]:
            each_cost = 0
            path.extend([city])
            
            # Recursive call
            each_cost,next_city = recur_sol(city_copy,costs, city,enter,[False]*len(visited)) 
            
            # Tag-2
            each_cost += costs[start][city]
            all_cost.append(each_cost)
            
            path.extend(next_city)
            all_path.append(path)

    # Tag-3 
    result_path.extend(all_path[all_cost.index(min(all_cost))])  

    # Tag-4
    if result_path[0] != enter:
        result_path.pop(0)
    else:
        result_path.append(enter)
    return min(all_cost),result_path

"""
Helping Documentation:

#Tag-1:
    The function is designed in such a way that the the <Tag-1> if condition will not get False.(Nothing special)
    Thus indenting the code blocks after <Tag-3> till return(excluding) under <Tag-3> if does not matter.
    It will  get executed regardless of <Tag-1> if condition.

#Tag-2 :
    The of each path from start to next_city calculated recursive manner. It is writtern after recursive call so that sub_paths+current_path can be done.
    Else the current_path cost will get erased on every recursive call.

#Tag-3 : 
    ```
    final_cost = min(all_cost)
    idx = all_cost.index(final_cost)
    final_path = all_path[idx]
    res_path.extend(final_path)
    ```
    
         Explaination: 
         The path and its cost is stored in corresponding position of all_path and all_cost.
         result_path already contains  starting city. [1] if start=1
         Extend the result_path with the path which has minimum of all_cost.

#Tag-4 : 
     This is just an adjustment code, else directly returning result path would lead to something like this = [1,2,2,3,3,4] etc
     To avoid this I've used the  code.
"""
