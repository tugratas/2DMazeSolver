from collections import deque

class Player:
    def __init__(self, maze, state_info):
        self.maze = maze
        self.state_info = state_info
        self.position = (2, 1)  # Initial position
        self.goal = None
        self.path = []  # To store the path taken
        self.allPath = [] # To store all paths taken
        self.visited = set()  # To store visited locations
        self.score = 0  # Reset the score
        self.goal_reached = None  # To store which goal state is reached when the goal is reached
        self.queue = deque()  # Queue for BFS

    def add_to_queue(self, position):
        if position not in self.visited:
            self.queue.append(position)
            self.visited.add(position)

    def get_new_position(self, direction):
        x, y = self.position
        if direction == 'up' and self.maze[x][y]['top']:
            return (x - 1, y)
        elif direction == 'down' and self.maze[x][y]['down']:
            return (x + 1, y)
        elif direction == 'left' and self.maze[x][y]['left']:
            return (x, y - 1)
        elif direction == 'right' and self.maze[x][y]['right']:
            return (x, y + 1)
        return None

    def is_valid_move(self, position):
        x, y = position
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


def breadth_first_search(player):
    start_position = player.position  # Store the starting position
    player.visited.add(player.position)  # Add the starting position to the visited set
    player.queue.append(player.position)  # Add the starting position to the queue
    parents = {player.position: None}  # To store where each node came from

    while player.queue:
        current_position = player.queue.popleft()
        player.position = current_position

        # Add the starting position to the allPath list
        if current_position != start_position:
            player.allPath.append(current_position)
            player.score += 1

        if player.is_goal(current_position):
         solution_path = reconstruct_path(parents, current_position)
         adjusted_solution_path = [(x+1, y+1) for x, y in solution_path]
         adjusted_all_path = [(x+1, y+1) for x, y in player.allPath]
         return adjusted_solution_path, player.score, player.goal_reached, adjusted_all_path

        for direction in ['right', 'down', 'left', 'up']:
            new_position = player.get_new_position(direction)
            if new_position and new_position not in player.visited:
                parents[new_position] = current_position
                player.add_to_queue(new_position)
                player.is_valid_move(new_position)  # Increase the score here

    return None, player.score, None, player.allPath


def reconstruct_path(parents, current):
    path = []
    while current is not None:
        if parents[current] is not None:  # Skip the starting position
            path.append(current)
        current = parents[current]
    path.reverse()  # Reverse to order from start to goal
    return path
