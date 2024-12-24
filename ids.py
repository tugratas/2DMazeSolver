class Player:
    def __init__(self, maze, state_info):
        self.maze = maze
        self.state_info = state_info
        self.position = (2, 1)  # Initial position
        self.goal = None
        self.path = []  # To store the path taken
        self.allPath = []  # To store all paths taken
        self.visited = set()  # To store the visited path
        self.score = 0  # Reset the score
        self.goal_reached = None  # To store which goal state is reached when the goal is reached

    def move(self, direction):
        x, y = self.position
        new_position = None

        if direction == 'up' and self.maze[x][y]['top']:
            new_position = (x - 1, y)
        elif direction == 'down' and self.maze[x][y]['down']:
            new_position = (x + 1, y)
        elif direction == 'left' and self.maze[x][y]['left']:
            new_position = (x, y - 1)
        elif direction == 'right' and self.maze[x][y]['right']:
            new_position = (x, y + 1)

        if new_position and self.is_valid_move(new_position) and new_position not in self.visited:
            self.score += 1  # Increase the score by 1 for each move
            self.position = new_position
            # Add to the path and allPath lists by adding +1 to the new position
            adjusted_position = (new_position[0] + 1, new_position[1] + 1)
            self.path.append(adjusted_position)
            self.allPath.append(adjusted_position)
            self.visited.add(new_position)
            return True

        return False  # Move is invalid or blocked

    def delete(self):
        self.path.pop()

    def is_valid_move(self, position):
        x, y = position
        # Check the value of the relevant cell in the state_info array
        cell_value = self.state_info[x][y]
        if cell_value == 'T':
            self.score += 6  # Increase the score by 6 in case of a trap
            return True
        return True

    def is_goal(self, position):
        x, y = position
        goal_states = ["G1", "G2", "G3", "G4", "G5"]
        if self.state_info[x, y] in goal_states:
            self.goal_reached = self.state_info[x, y]
            return True
        return False


def iterative_deepening_search(player):
    for depth in range(50):
        # Reset the player's initial state in each iteration
        player.position = (2, 1)
        player.path = [(3, 2)]
        player.visited = set([(2, 1)])
        player.score = 0
        player.goal_reached = None
        result = depth_limited_search(player, depth)
        if result[2]:  # If the goal is found
            return result
    return None, player.score, None, player.allPath

def depth_limited_search(player, limit, current_depth=0, start_position=None):
    if start_position is None:
        start_position = player.position

    current_position = player.position
    if current_position == start_position and current_depth > 0:
        return None, player.score, None, player.allPath

    if player.is_goal(current_position):
        return player.path, player.score, player.goal_reached, player.allPath

    if current_depth == limit:
        return None, player.score, None, player.allPath

    for direction in ['right', 'down', 'left', 'up']:
        if player.move(direction):
            result = depth_limited_search(player, limit, current_depth + 1, start_position)
            if result[2]:  # If the goal is found
                return result
            player.delete()
            player.position = current_position

    return None, player.score, None, player.allPath