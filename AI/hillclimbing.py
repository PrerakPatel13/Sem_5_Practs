import copy
visited_states = []
def gn(curr_state,prev_heu,goal):
    global visited_states
    state = copy.deepcopy(curr_state)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    curr_heu=heuristic(temp1,goal)
                    if curr_heu>prev_heu:
                        child = copy.deepcopy(temp1)
                        return child
    return 0

def heuristic(curr_state,goal):
    copygoal=goal[3]
    val=0
    for i in range(len(curr_state)):
        check_val=curr_state[i]
        if len(check_val)>0:
            for j in range(len(check_val)):
                if check_val[j]!=copygoal[j]:
                    val-=j
                else:
                    val+=j
    print(f"Heuristic value for {curr_state} is {val}")
    return val
 
def sln(init_state,goal):
    global visited_states
    if (init_state == goal):
        print(f"Solution found! {goal}\n")
        return
    current = copy.deepcopy(init_state)
 
    while(True):
        visited_states.append(copy.deepcopy(current))
        print(f"Current State : {current}")
        prev_heu=heuristic(current,goal)
        child = gn(current,prev_heu,goal)
        
        if child==0:
            print(f"No heuristic value is obtained better than this thus declaring this as goal state - {current}\n")
            return
        print(f"Child chosen for exploration : {child}\n")        
        current = copy.deepcopy(child)
 
def main():
    global visited_states
    initial = [[],[],[],['B','C','D','A']]
    goal = [[],[],[],['A','B','C','D']]
    sln(initial,goal)
main()