graph = {
    'A': {'B': 6, 'F': 3},
    'B': {'C': 3,'D': 2},
    'C': {'D': 1,'E': 5},
    'D': {'E': 8},
    'E': {'I': 5,'J': 5},
    'F': {'G': 1,'H': 7},
    'G': {'I': 3},
    'H': {'I': 2},
    'I': {'J': 3},
    'J': {}
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0,
}


current = "A"
goal = "J"

def searchlist(l,k):
    for i in l:
        if i[0] == k:
            return i

def funcofn(gl,cn): 
    g =0
    for i in range(len(gl)-1):
        g += graph[gl[i]][gl[i+1]]
    g += graph[gl[-1]][cn] + heuristic[cn]
    return g

open_list = []
close_list = []
open_list.append([current,heuristic[current],[current]])
n = 0 
try:
    while True:
        parent = open_list[0][0]
        close_list.append(parent)
        current_path = open_list[0][2]
        if parent == goal:
            break
        print(f"Currently at node : {parent}")
        for j in graph[open_list[0][0]]:
            open_list.append([j,funcofn(current_path,j),current_path+[j]])
            open_list = sorted(open_list, key=lambda x: x[1])
        open_list = [pair for pair in open_list if pair[0] != parent]
        n+=1   
        print(f"Open List is : {open_list}\nclosed List is : {close_list}\n")
except:
    print("Node not Found")        

print(f"Solution path is from {open_list[0][2][0]} to {goal} is {open_list[0][2]} with distance : {open_list[0][1]}")