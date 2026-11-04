
from maze_solver import solve_maze


def print_legend():
    print("\nMaze Symbols:")
    print("S = Start (Starting point)")
    print("E = End (Ending point)")
    print("# = Wall (Blocked cell)")
    print(". = Empty cell (Free space)")
    print("* = Solution path found by BFS")


def print_maze(maze, path=None):
    if path is None:
        path = []

    for r in range(len(maze)):
        row = ""

        for c in range(len(maze[0])):
            if (r, c) in path and maze[r][c] not in ("S", "E"):
                row += "* "
            else:
                row += maze[r][c] + " "

        print(row)


maze = [
    ["S", ".", "#", ".", "."],
    ["#", ".", "#", ".", "#"],
    [".", ".", ".", ".", "#"],
    [".", "#", "#", ".", "."],
    [".", ".", ".", ".", "E"]
]

print("=" * 35)
print("       MAZE SOLVER USING BFS")
print("=" * 35)

print_legend()

print("\nOriginal Maze:")
print_maze(maze)

path = solve_maze(maze)

print("\nSolution:")

if path:
    print_maze(maze, path)
    print("\nPath found!")
    print("Path length:", len(path) - 1)
    print("Path:", path)
else:
    print("No path found!")
