import heapq

class Player:
    def __init__(self, maze, state_info):
        self.maze = maze
        self.state_info = state_info
        self.position = (2, 1)  # Initial position
        self.goal = None
        self.allPath = []  # To store all paths taken
        self.goal_reached = None  # To store which goal state is reached when the goal is reached

    def get_next_position(self, direction):
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

    def is_goal(self, position):
        x, y = position
        goal_states = ["G1", "G2", "G3", "G4", "G5"]
        if self.state_info[x, y] in goal_states:
            self.goal_reached = self.state_info[x, y]
            return True
        return False


def uniform_cost_search(player):
    # Initialize the priority queue (minimum heap)
    priority_queue = []
    heapq.heappush(priority_queue, (0, player.position))  # (cost, position)

    # Dictionary to store costs
    costs = {player.position: 0}
    parents = {player.position: None}  # To store where each node came from

    while priority_queue:
        current_cost, current_position = heapq.heappop(priority_queue)

        # Check if the goal is reached
        if player.is_goal(current_position):
            return reconstruct_path(parents, current_position), current_cost, player.goal_reached, player.allPath

        player.position = current_position

        for direction in ['right', 'down', 'left', 'up']:
            next_position = player.get_next_position(direction)
            if next_position:
                new_cost = current_cost + calculate_cost(player, next_position)
                if next_position not in costs or new_cost < costs[next_position]:
                    costs[next_position] = new_cost
                    parents[next_position] = current_position
                    heapq.heappush(priority_queue, (new_cost, next_position))

    return None, None, None, player.allPath


def calculate_cost(player, position):
    # This function calculates the cost for a specific position
    x, y = position
    if player.state_info[x][y] == 'T':
        return 7  # Extra cost for traps
    return 1  # Normal step cost


def reconstruct_path(parents, current):
    path = []
    while current is not None:
        adjusted_position = (current[0] + 1, current[1] + 1)
        path.append(adjusted_position)
        current = parents[current]
    path.reverse()
    return path