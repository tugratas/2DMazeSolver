from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Actual cost
        self.h = 0  # Heuristic cost
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

class Player:
    def __init__(self, maze, state_info, start_position, goal_positions):
        self.maze = maze
        self.state_info = state_info
        self.position = start_position
        self.goal_positions = goal_positions
        self.path = []
        self.allPath = []
        self.visited = set()
        self.score = 0
        self.goal_reached = None

    def get_new_position(self, direction):
        x, y = self.position
        if x < 0 or y < 0 or x >= len(self.maze) or y >= len(self.maze[0]):
            return None

        new_position = None
        if direction == 'up' and self.maze[x][y]['top']:
            new_position = (x - 1, y)
        elif direction == 'down' and self.maze[x][y]['down']:
            new_position = (x + 1, y)
        elif direction == 'left' and self.maze[x][y]['left']:
            new_position = (x, y - 1)
        elif direction == 'right' and self.maze[x][y]['right']:
            new_position = (x, y + 1)

        # Trap check
        if self.state_info[x][y] == 'T':
            self.score += 6  # Extra cost for traps

        return new_position

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(player):
    start_node = Node(player.position)
    end_nodes = [Node(pos) for pos in player.goal_positions]

    open_set = PriorityQueue()
    open_set.put((0, start_node))
    came_from = {start_node.position: None}

    g_score = {start_node.position: 0}
    f_score = {start_node.position: heuristic(start_node.position, end_nodes[0].position)}

    while not open_set.empty():
        current_node = open_set.get()[1]
        player.position = current_node.position

        if player.position in [node.position for node in end_nodes]:
            player.goal_reached = player.state_info[current_node.position]
            path, score = reconstruct_path(came_from, current_node, player.state_info)
            return path, score, player.goal_reached, player.allPath

        player.visited.add(current_node.position)
        player.allPath.append(current_node.position)
        player.score += 1

        if player.state_info[player.position[0]][player.position[1]] == 'T':
            player.score += 6

        for direction in ['right', 'down', 'left', 'up']:
            new_position = player.get_new_position(direction)
            if new_position is None or new_position in player.visited:
                continue

            tentative_g_score = g_score[current_node.position] + 1
            if tentative_g_score < g_score.get(new_position, float("inf")):
                came_from[new_position] = current_node
                g_score[new_position] = tentative_g_score
                f_score[new_position] = tentative_g_score + heuristic(new_position, end_nodes[0].position)
                if new_position not in [node[1].position for node in open_set.queue]:
                    open_set.put((f_score[new_position], Node(new_position, current_node)))

    return [], float("inf"), None, player.allPath


def reconstruct_path(came_from, current_node, state_info):
    total_path = []
    score = 0

    # Check for traps while constructing the solution path
    while current_node is not None:
        position = current_node.position
        total_path.append(position)

        # If the current position is a trap, increase the score
        if state_info[position[0]][position[1]] == 'T':
            score += 6

        current_node = came_from.get(position)

    total_path.reverse()
    return total_path, score
