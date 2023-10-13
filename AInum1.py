def solve_maze(maze):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "1"

    def get_neighbors(x, y):
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = [(x + dx, y + dy) for dx, dy in deltas]
        return [(nx, ny) for nx, ny in neighbors if is_valid(nx, ny)]

    def print_maze_with_path(maze, path):
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if (i, j) in path:
                    if (i, j) == path[-1]:
                        print("G", end=" ")
                    else:
                        print("X", end=" ")
                else:
                    print(maze[i][j], end=" ")
            print()

    start = None
    goal = None

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "G":
                goal = (i, j)

    if start is None or goal is None:
        return "Start or goal not found in the maze."

    queue = [(start, [])]
    visited = set()
    visited.add(start)  # Mark the start position as visited.

    while queue:
        (x, y), path = queue.pop(0)

        if (x, y) == goal:
            print_maze_with_path(maze, path)
            return

        for (nx, ny) in get_neighbors(x, y):
            if (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))  # Mark the neighbor as visited immediately.

    return "No path found."

maze = [
    ["S", "1", "0", "0", "0", "0", "0", "1", "0"],
    ["0", "1", "0", "1", "1", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "G", "0", "0", "1", "0"],
    ["0", "1", "0", "1", "1", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "0", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["0", "1", "0", "0", "0", "0", "0", "0", "0"]
]

solve_maze(maze)


