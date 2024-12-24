import heapq

class Player:
    def __init__(self, maze, state_info):
        self.maze = maze
        self.state_info = state_info
        self.position = (3, 2)  # Initial position
        self.goal_states = [(2,6),(5,6),(7,7),(7,4),(6,1)]
        self.path = []  # To store the path taken
        self.allPath = []  # To store all paths taken
        self.score = 0  # Reset the score
        self.goal_reached = None  # To store which goal state is reached when the goal is reached


    def is_valid_move(self, position):
        x, y = position
        return self.state_info[x][y] != 'T'  # Any cell that is not a trap is valid

    def is_goal(self, position):
       
        x, y = position
        goal_states = ["G1", "G2", "G3", "G4", "G5"]
        if self.state_info[x, y] in goal_states:
            self.goal_reached = self.state_info[x, y]
            return True
        return False

    def get_new_position(self, direction):
        x, y = self.position
        next_position = None

        if direction == 'up' and self.maze[x][y]['top']:
            next_position = (x - 1, y)
        elif direction == 'down' and self.maze[x][y]['down']:
            next_position = (x + 1, y)
        elif direction == 'left' and self.maze[x][y]['left']:
            next_position = (x, y - 1)
        elif direction == 'right' and self.maze[x][y]['right']:
            next_position = (x, y + 1)

        if next_position is not None:
            adjusted_position = (next_position[0] + 1, next_position[1] + 1)
            self.allPath.append(adjusted_position)
        return next_position

def greedy_best_first_search(player):
    priority_queue = []
    heapq.heappush(priority_queue, (0, player.position))

    visited = set()
    parents = {player.position: None}

    while priority_queue:
        _, current_position = heapq.heappop(priority_queue)

        if current_position in visited:
            continue

        visited.add(current_position)
        player.position = current_position

        if player.is_goal(current_position):
            return reconstruct_path(parents, current_position), player.score, player.goal_reached, player.allPath

        for direction in ['right', 'down', 'left', 'up']:
            new_position = player.get_new_position(direction)
            if new_position and new_position not in visited:
                heuristic_value = calculate_heuristic(new_position, player.goal_states)
                heapq.heappush(priority_queue, (heuristic_value, new_position))
                parents[new_position] = current_position
    return None, player.score, None, player.allPath


def calculate_heuristic(position, goal_states):
    # Calculates the estimated distance to the goal using the Manhattan distance
    return min(abs(position[0] - goal[0]) + abs(position[1] - goal[1]) for goal in goal_states)

def reconstruct_path(parents, current):
    path = []
    while current is not None:
        adjusted_position = (current[0] + 1, current[1] + 1)
        path.append(adjusted_position)
        current = parents[current]
    path.reverse()
    return path