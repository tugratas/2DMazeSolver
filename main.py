import numpy as np


#Maze information for moving Left , Right , Top , Bottom
mazeDictionary = [
    [ ##1
        {'top': False, 'left': False, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': False, 'down': True},
        {'top': False, 'left': False, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': True, 'down': False},
        {'top': False, 'left': True, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': True, 'down': False},
        {'top': False, 'left': True, 'right': True, 'down': False},
        {'top': False, 'left': True, 'right': False, 'down': True}
    ],
    [ ##2
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': True, 'down': False},
        {'top': True, 'left': True, 'right': True, 'down': False},
        {'top': False, 'left': True, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': False, 'left': False, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': True, 'down': False},
        {'top': True, 'left': True, 'right': False, 'down': True}
    ],
    [ ##3
        {'top': True, 'left': False, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': False, 'down': True},
        {'top': False, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': True, 'down': False},
        {'top': True, 'left': True, 'right': True, 'down': False},
        {'top': True, 'left': True, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': False, 'down': False},
        {'top': True, 'left': False, 'right': False, 'down': True}
    ],
    [ ##4
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': True, 'down': True},
        {'top': True, 'left': True, 'right': False, 'down': True},
        {'top': False, 'left': False, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': False, 'left': False, 'right': True, 'down': False},
        {'top': True, 'left': True, 'right': False, 'down': True}
    ],
    [ ##5
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': False},
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': False, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': True},
    ],
    [ ##6
        {'top': True, 'left': False, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': True, 'down': False},
        {'top': True, 'left': True, 'right': True, 'down': False},
        {'top': True, 'left': True, 'right': False, 'down': False},
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': True, 'down': False},
        {'top': True, 'left': True, 'right': False, 'down': True}
    ],
    [ ##7
        {'top': True, 'left': False, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': True, 'down': False},
        {'top': False, 'left': True, 'right': True, 'down': True},
        {'top': False, 'left': True, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': False},
        {'top': True, 'left': False, 'right': True, 'down': False},
        {'top': False, 'left': True, 'right': False, 'down': True},
        {'top': True, 'left': False, 'right': False, 'down': True}
    ],
    [ ##8
        {'top': True, 'left': False, 'right': True, 'down': False},
        {'top': False, 'left': True, 'right': False, 'down': False},
        {'top': True, 'left': False, 'right': False, 'down': False},
        {'top': True, 'left': False, 'right': False, 'down': False},
        {'top': False, 'left': False, 'right': True, 'down': False},
        {'top': False, 'left': True, 'right': True, 'down': False},
        {'top': True, 'left': True, 'right': False, 'down': False},
        {'top': True, 'left': False, 'right': False, 'down': False}
    ],
]

#Trap and Goal States Informations
stateInfo = np.full((8, 8), None, dtype='object')
#Trap States
stateInfo[1][3] = "T"
stateInfo[2][5] = "T"
stateInfo[3][0] = "T"
stateInfo[3][1] = "T"
stateInfo[4][2] = "T"
stateInfo[5][0] = "T"
stateInfo[6][0] = "T"
stateInfo[6][5] = "T"
stateInfo[6][7] = "T"

#Goal States
stateInfo[2][6] = "G1"
stateInfo[5][6] = "G2"
stateInfo[7][7] = "G3"
stateInfo[7][4] = "G4"
stateInfo[6][1] = "G5"


stateInfo[2][1] = "S"
# We are asking the user which search algorithm they want to use.
print("Please select an algorithm:")
print("1: Depth First Search (DFS)")
print("2: Breadth First Search (BFS)")
print("3: Iterative Deepening Search (IDS)")
print("4: Uniform Cost Search (UCS)")
print("5: Greedy Best First Search (GBFS)")
print("6: A* Search (A*)")
choice = input("Enter your choice (1-6): ")

# Depending on the choice, we invoke the relevant search algorithm.
if choice == '1': # Depth First Search
    from dfs import Player,depth_first_search
    player = Player(mazeDictionary, stateInfo)
    result,score,goal_reached,allPath = depth_first_search(player)
    print("The solution path:", result)
    print("The cost of the solution path: ",score)
    print("The goal State: ",goal_reached)
    print("The list of expanded nodes:", allPath)
elif choice == '2': # Breadth First Search
    from bfs import breadth_first_search, Player
    player = Player(mazeDictionary, stateInfo) 
    result, score, goal_reached, allPath = breadth_first_search(player)  
    print("The solution path:", result)
    print("The cost of the solution path: ", score)
    print("The goal State: ", goal_reached)
    print("The list of expanded nodes:", allPath)
elif choice == '3': # Iterative Deepening
    from ids import iterative_deepening_search, Player
    player = Player(mazeDictionary, stateInfo)  
    result, score, goal_reached, allPath = iterative_deepening_search(player) 
    print("The solution path:", result)
    print("The cost of the solution path: ", score)
    print("The goal State: ", goal_reached)
    print("The list of expanded nodes:", allPath)
elif choice == '4': # Uniform Cost Search
    from ucs import uniform_cost_search, Player
    player = Player(mazeDictionary, stateInfo)  
    result, score, goal_reached, allPath = uniform_cost_search(player)  
    print("The solution path:", result)
    print("The cost of the solution path: ", score)
    print("The goal State: ", goal_reached)
    print("The list of expanded nodes:", allPath)
elif choice == '5': # Greedy Best First Search
    from greedybfs import greedy_best_first_search, Player
    player = Player(mazeDictionary, stateInfo) 
    result, score, goal_reached, allPath = greedy_best_first_search(player)  
    print("The solution path:", result)
    print("The cost of the solution path: ", score)
    print("The goal State: ", goal_reached)
    print("The list of expanded nodes:", allPath)
elif choice == '6': # A* Heuristic Search
    from astar import astar_search, Player
    player = Player(mazeDictionary, stateInfo, start_position=(2, 1), goal_positions=[(2, 6), (5, 6), (7, 7), (7, 4), (6, 1)])
    result, score, goal_reached, allPath = astar_search(player)
    print("The solution path:", result)
    print("The cost of the solution path: ", score)
    print("The goal State: ", goal_reached)
    print("The list of expanded nodes:", allPath)


