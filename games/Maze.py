#class Maze:
    # def __init__(self, board = [[]]):
    #     self.board = board
    #     self.memo = []
    #     for i in range(len(self.board)):
    #         self.memo.append([])
    #         for j in range(len(self.board)):
    #             self.memo[i].append('unvisited')

    # def oob(self,i,j):
    #     if i < 0 or i >= len(self.board):
    #         return True

    #     if j < 0 or j >= len(self.board[0]):
    #         return True

    #     return False

    # def at_end(self,i,j):
    #     return i == len(self.board) - 1 and j == len(self.board[0]) - 1

    # def gen_next_points(self,i,j):
    #     points = []
    #     points.append([i+1,j])
    #     points.append([i-i,j])
    #     points.append([i,j+1])
    #     points.append([i,j-1])

    #     return points

    # def update_memo(self, i,j, value):
    #     self.memo[i][j] = value

    # def solve(self, i,j):

    #     if self.oob(i,j) or self.board[i][j] == 1:
    #         return False

    #     if self.at_end(i,j):
    #         return True

    #     if self.memo[i][j] in ['no_path_found', 'visiting']:
    #         return False

    #     self.update_memo(i,j, 'visiting')

    #     points = self.gen_next_points(i,j)
    #     for point in points:
    #         if self.solve(*point):
    #             return True

    #     self.update_memo(i,j, 'no_path_found')

    #     return False

    # def solveBoard(self):
    #     return self.solve(0,0)

class Maze:
    def __init__(self, board = [[]]):
        self.board = board
        self.size = len(board)
        self.memo = []
        for i in range(self.size):
            self.memo.append([])
            for j in range (self.size):
                self.memo[i].append('unvisited')

    def oob(self,i,j):
        if i < 0 or i >= self.size:
            return True
        if j < 0 or j >= self.size:
            return True
        return False

    def at_end(self,i,j):
        return i == self.size - 1 and j == self.size - 1

    def gen_next_points(self, i,j):
        points = []
        points.append([i + 1, j])
        points.append([i - 1, j])
        points.append([i, j + 1])
        points.append([i, j - 1])
        return points

    def solve(self,i,j):
        if self.oob(i,j) or self.board[i][j] == 1:
            return False

        if self.at_end(i,j):
            return True

        if self.memo[i][j] in ['no_path_found', 'visiting']:
            return False

        self.memo[i][j] = 'visiting'

        points = self.gen_next_points(i,j)
        for point in points:
            if self.solve(*point):
                return True

        self.memo[i][j] = 'no_path_found'

        return False

    def solveBoard(self):
        return self.solve(0,0)
