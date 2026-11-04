from collections import deque


def solve_maze(maze):
    """
    Find the shortest path in a maze using BFS.

    Maze Symbols:
    S = Start
    E = End
    # = Wall
    . = Empty cell
    * = Solution path (display only)
    """

    rows = len(maze)

    if rows == 0:
        return None

    cols = len(maze[0])

    if cols == 0 or any(len(row) != cols for row in maze):
        return None

    start = None
    end = None

    # Find start and end positions
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start = (r, c)
            elif maze[r][c] == "E":
                end = (r, c)

    if start is None or end is None:
        return None

    queue = deque([(start, [start])])
    visited = {start}

    # Possible movements: up, down, left, right
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and maze[nr][nc] != "#"
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None
