graph = {
    'A': ['B','C','D'],
    'B': ['E','F','A'],
    'C': ['G','H','A'],
    'D': ['I','A'],
    'E': ['J','K','B'],
    'F': ['B'],
    'G': ['L','C'],
    'H': ['C'],
    'I': ['M','D'],
    'J': ['E'],
    'K': ['N','E'],
    'L': ['G'],
    'M': ['I'],
    'N': ['K']
}


def dfid(graph, current, goal, visited, path, depth):
    for i in range(1,depth+1):
        print(f"Depth : {i}")
        print(f"Visited\t\tNot Visited\t\tGoal State")
        path, state = dfs(graph, current, goal, [], [], 0, i)
        
    return path, state

def dfs(graph, current, goal, visited, path, curr_depth, depth):
    if curr_depth<=depth:
        if current not in visited:
            path.append(current)
            visited.append(current)
            not_visited = [i for i in graph.keys() if i not in visited]
            if current == goal:
                print(f"{' '.join(visited)}\t\t{' '.join(not_visited)}\t\tTrue")
                return path,True
            
            print(f"{' '.join(visited)}\t\t{' '.join(not_visited)}\t\tFalse")
            for i in graph[current]:
                path, state = dfs(graph, i, goal, visited, path, curr_depth+1, depth)
                if state == True:
                    return path, True
                
        return path,False
    else:
        return path,False

path1, state =  dfid(graph,'A','N',[],[],4)


if state:
    print(f"Element Found \nPath = {path1}")
else:
    print("Element not found")