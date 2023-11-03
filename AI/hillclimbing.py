import copy
visited = []
def gn(current,prev_heu,goal):
    global visited
    state = copy.deepcopy(current)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    if (temp1 not in visited):
                        curr_heu=heuristic(temp1,goal)
                        if curr_heu>prev_heu:
                            child = copy.deepcopy(temp1)
                            return child
 
    return 0
def heuristic(current,goal):
    goalc=goal[3]
    val=0
    for i in range(len(current)):
        check_val=current[i]
        if len(check_val)>0:
            for j in range(len(check_val)):
                if check_val[j]!=goalc[j]:
                    val-=j
                else:
                    val+=j
    return val
 
def sln(init_state,goal):
    global visited
    if (init_state == goal):
        print (goal)
        print("solution found!")
        return
    current_state = copy.deepcopy(init_state)
 
    while(True):
        visited.append(copy.deepcopy(current_state))
        print(current_state)
        prev_heu=heuristic(current_state,goal)
        child = gn(current_state,prev_heu,goal)
        if child==0:
            print("Final state - ",current_state)
            return
 
        current_state = copy.deepcopy(child)
 
def main():
    global visited
    initial = [[],[],[],['B','C','D','A']]
    goal = [[],[],[],['A','B','C','D']]
    sln(initial,goal)
import copy
visited = []
def gn(current,prev_heu,goal):
    global visited
    state = copy.deepcopy(current)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    if (temp1 not in visited):
                        curr_heu=heuristic(temp1,goal)
                        if curr_heu>prev_heu:
                            child = copy.deepcopy(temp1)
                            return child
 
    return 0
def heuristic(current,goal):
    goalc=goal[3]
    val=0
    for i in range(len(current)):
        check_val=current[i]
        if len(check_val)>0:
            for j in range(len(check_val)):
                if check_val[j]!=goalc[j]:
                    val-=j
                else:
                    val+=j
    return val
 
def sln(init_state,goal):
    global visited
    if (init_state == goal):
        print (goal)
        print("solution found!")
        return
    current_state = copy.deepcopy(init_state)
 
    while(True):
        visited.append(copy.deepcopy(current_state))
        print(current_state)
        prev_heu=heuristic(current_state,goal)
        child = gn(current_state,prev_heu,goal)
        if child==0:
            print("Final state - ",current_state)
            return
 
        current_state = copy.deepcopy(child)
 
def main():
    global visited
    initial = [[],[],[],['B','C','D','A']]
    goal = [[],[],[],['A','B','C','D']]
    sln(initial,goal)
main()