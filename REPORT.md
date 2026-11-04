# \# Maze Solver Project Report

# 

# \## 1. Introduction

# 

# The Maze Solver project aims to find the shortest path between a starting point and an ending point in a maze.

# 

# The project uses the Breadth-First Search (BFS) algorithm to solve the maze efficiently.

# 

# \## 2. Maze Symbols

# 

# The maze is represented using five symbols:

# 

# \- S: Starting point.

# \- E: Ending point.

# \- #: Wall that cannot be crossed.

# \- .: Empty cell that can be visited.

# \- \*: Solution path found by BFS.

# 

# These symbols make the maze easy to read and understand.

# 

# \## 3. Graph Representation

# 

# The maze is represented as a two-dimensional grid.

# 

# Each cell that is not a wall represents a vertex (node), and connections between adjacent cells represent edges.

# 

# Walls cannot be visited.

# 

# The allowed movements are:

# 

# \- Up

# \- Down

# \- Left

# \- Right

# 

# \## 4. Algorithm

# 

# The project uses Breadth-First Search (BFS).

# 

# BFS explores all neighboring cells before moving to the next level.

# 

# A queue is used to manage the cells waiting to be explored. A visited set prevents visiting the same cell more than once.

# 

# When the ending point is reached, the algorithm returns the path from the starting point to the ending point.

# 

# \## 5. Complexity Analysis

# 

# Let V represent the number of open cells and E represent the number of possible connections.

# 

# Time Complexity: O(V + E)

# 

# Space Complexity: O(V)

# 

# \## 6. Experiments and Testing

# 

# The project was tested using three unit tests:

# 

# 1\. Finding a valid path.

# 2\. Checking a maze with no available path.

# 3\. Checking a maze without start and end points.

# 

# All three unit tests passed successfully after the symbol update.

# 

# \## 7. Conclusion

# 

# The project demonstrates how BFS can solve maze problems and find the shortest path in an unweighted graph.

# 

# It also provides practical experience with graph traversal, queues, visited nodes, and unit testing.

