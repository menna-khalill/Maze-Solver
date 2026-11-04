# Maze Solver Using BFS

## Project Description

Maze Solver is a Python project that finds the shortest path from a starting point to an ending point in a maze.

The project uses the Breadth-First Search (BFS) algorithm to explore the maze and find the shortest possible path.

## Maze Symbols (Legend)

The maze uses the following symbols:

| Symbol | Meaning | Description |
|---|---|---|
| S | Start | Starting point of the maze |
| E | End | Destination point |
| # | Wall | Blocked cell that cannot be crossed |
| . | Empty | Free cell that can be visited |
| * | Path | Path found by the BFS algorithm |

## Algorithm

Breadth-First Search (BFS) is a graph traversal algorithm that explores neighboring nodes level by level.

It guarantees finding the shortest path in an unweighted graph.

## Allowed Movements

The algorithm can move in four directions:

- Up
- Down
- Left
- Right

## Project Structure

- main.py: Runs the maze solver and displays the maze.
- maze_solver.py: Contains the BFS algorithm.
- test_maze_solver.py: Contains unit tests.
- README.md: Project documentation.
- REPORT.md: Project report.
- REFLECTION.md: Project reflection.

## How to Run

Make sure Python is installed.

Open the project folder in the terminal and run:

    python main.py

## How to Run Tests

Run:

    python -m unittest -v

## Time and Space Complexity

Let V be the number of open cells and E be the number of possible connections between them.

- Time Complexity: O(V + E)
- Space Complexity: O(V)

## Technologies Used

- Python
- Breadth-First Search (BFS)
- Unit Testing