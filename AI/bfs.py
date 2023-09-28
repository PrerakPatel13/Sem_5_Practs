graph = {
    'S': ['A', 'B', 'D'],
    'A': ['S', 'E'],
    'B': ['S', 'E'],
    'D': ['S', 'G'],
    'E': ['A', 'B', 'F'],
    'F': ['E', 'G'],
    'G': ['D', 'F']
}

visited = []
queue = []
closed_list = []
path = {}
goal_state = "False"

def bfs(visited, graph, node, goal):
    visited.append(node)
    queue.append(node)
    path[node] = node
    print("Open List\tClose List\tGoal State")
    print(f"{' '.join(queue)}\t\t{' '.join(closed_list)}\t\tFalse")
    while queue:
        find = queue.pop(0)

        if find == goal:
            root = []
            while path[find] != find:
                root.append(find)
                find = path[find]
            root.append(find)
            root.reverse()
            print(f"{' '.join(queue)}\t\t{' '.join(closed_list)}\t\tTrue")
            print(f'Element Found')
            print(f'Path: {root}')
            return

        closed_list.append(find)

        for neighbour in graph[find]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                path[neighbour] = find

            if find == goal:
               goal_state = "True"
            else:
               goal_state = "False"
        print(f"{' '.join(queue)}\t\t{' '.join(closed_list)}\t\t{goal_state}")
    if goal_state == "False":
        print(f'Element not found')

print("Breadth-First Search")
print("\n")
bfs(visited, graph, 'S', 'E')

