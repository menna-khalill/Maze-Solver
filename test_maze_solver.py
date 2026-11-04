import unittest
from maze_solver import solve_maze


class TestMazeSolver(unittest.TestCase):

    def test_find_path(self):
        maze = [
            ["S", ".", "#"],
            ["#", ".", "."],
            [".", ".", "E"]
        ]

        path = solve_maze(maze)

        self.assertIsNotNone(path)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (2, 2))

    def test_no_path(self):
        maze = [
            ["S", "#", "E"],
            ["#", "#", "#"]
        ]

        path = solve_maze(maze)

        self.assertIsNone(path)

    def test_missing_start_and_end(self):
        maze = [
            [".", "."],
            [".", "."]
        ]

        path = solve_maze(maze)

        self.assertIsNone(path)


if __name__ == "__main__":
    unittest.main()
