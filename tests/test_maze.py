import unittest

from games import Maze

class TestMaze(unittest.TestCase):
    def test_it_is_a_maze(self):
        board = [[0,1,1,1],[0,1,1,1],[0,0,0,0],[1,1,1,0]]
        maze = Maze(board)
        self.assertIsInstance(maze, Maze)

    def test_it_solves_a_maze(self):
        board = [[0,1,1,1],[0,1,1,1],[0,0,0,0],[1,1,1,0]]
        maze = Maze(board)
        r = maze.solveBoard()
        self.assertEqual(r,True)

if __name__ == '__main__':
    unittest.main()
