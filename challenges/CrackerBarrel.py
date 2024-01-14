# Senior SW Engineer reporting Tim
# Start on the 10th, 18th
# Base: 150k
# signing:5k
# equity:
# 20,000 vest over 4 years. strike price 38c/share
# round E, 2009 (200,000,000)
# 155 5k 18k; 160k, 0, 16k; 160k, 5k 10k shares
# anualize target bonus: 7.5%:: (twice per year)
# matching 401k match upto 3k
# unlimited PTO (expect 3 - 4 weeks):
# benefits (100%, anthhem blue cross) -- covered on 10th
# tertiary: gym memberships, caltrain go-pass
import copy

class Puzzle:
    solutions = []
    forward = 1
    """
    Peg board puzzle

    The board attribute stores the current state of the board such that
    a tuple (x,y) representing a position on the board can be accessesed
    at board[y][x]. All position tuples are shown in the diagram below

    0,4
    0,3 1,3
    0,2 1,2 2,2
    0,1 1,1 2,1 3,1
    0,0 1,0 2,0 3,0 4,0

    Captures can happen in six directions
    x,y to x+2,y, removing x+1,y
    x,y to x-2, y, removing x-1,y
    """
    def __init__(self, x = 0, y = 0, board = None, num_pegs = 0, history = []):
        self.start_peg = (x,y)
        if board:
            self.board = board
            self.pegs_remaining = num_pegs
            self.history = history
            return

        """init board with one empty peg"""
        self.board = []
        for row in range(5):
            self.board.append([])
            for col in range(5 - row):
                self.board[row].append(True)

        self.pegs_remaining = 15

        self._remove(x,y)

        self.history = []

    def __str__(self):

        str = ""
        for row in reversed(self.board):
            for _ in range(5 - len(row)):
                str += " "
            for peg in row:
                if peg:
                    str += " *"
                else:
                    str += " -"

            str += "\n"

        return str

    def __contains__(self,peg):
        x = peg[0]
        y = peg[1]

        if x < 0 or y < 0:
            raise self.PegError("There is no hole at %s,%s" % (x,y))

        try:
            p = self.board[y][x]
        except:
            raise self.PegError("There is no hole at %s,%s" % (x,y))

        return p

    def show_moves(self):
        p = Puzzle(self.start_peg[0], self.start_peg[1])

        s = str(p)

        for move in self.history:
            p.move(move)
            s += "\n\n" + str(p)

        return s + "\n\nSolved in %s moves." % len(self.history)

    def _remove(self,x,y):
        """Remove peg at coordinates"""
        if not (x,y) in self:
            raise self.PegError("There is not peg to remove at %s,%s" % (x,y))

        self.board[y][x] = False
        self.pegs_remaining -= 1

    def _add(self,x,y):
        """Add a peg at coordinates"""
        if (x,y) in self:
            raise self.PegError("There is already a peg at at %s,%s" % (x,y))

        self.board[y][x] = True
        self.pegs_remaining += 1

    def move(self, move):
        """Move a peg and remove the jumped peg"""

        # get move values
        x = move.x
        y = move.y
        d = move.direction

        # always start by removing the peg we're moving
        self._remove(x, y)

        # move forward
        if d == 1:
            self._remove(x + 1, y)
            self._add(x + 2, y)

        # move back
        elif d == 2:
            self._remove(x - 1, y)
            self._add(x - 2, y)

        # move up
        elif d == 3:
            self._remove(x, y + 1)
            self._add(x, y + 2)

        # move down
        elif d == 4:
            self._remove(x, y - 1)
            self._add(x, y - 2)

        # move down and forward
        elif d == 5:
            self._remove(x + 1, y - 1)
            self._add(x + 2, y - 2)

        # move up and back
        elif d == 6:
            self._remove(x - 1, y + 1)
            self._add(x - 2, y + 2)

        # add the move we just made to this board's history
        self.history.append(move)

    def solve(self):
        """Find all? possible solutions from current board config"""

        # iterate over all peg holes in board
        for y,row in enumerate(self.board):
            for x,peg in enumerate(row):
                if not peg: continue

                # iterate over all possible directions
                for direction in range(1,7):

                    # make a copy of the board to test the move on
                    branch = Puzzle(self.start_peg[0], self.start_peg[1], [r[:] for r in self.board], self.pegs_remaining, self.history[:])

                    try:
                        branch.move(Puzzle.Move(x,y, direction))

                        if branch.pegs_remaining == 1:
                            return branch #solved!
                        else:
                            return branch.solve()

                    # just skip an invalid move
                    except Exception as err:
                        continue

        raise self.DeadEnd(f"Deadend pegs remaining = {branch.pegs_remaining}")

    class DeadEnd(Exception):
        """We've run out of possible moves and puzzle is not solved"""

    class PegError(Exception):
        """Exception for when unable to add/remove peg"""


    class Move:
        """An object to store a single peg move"""
        def __init__(self,x, y, direction):
            self.x = x
            self.y = y
            self.direction = direction

            # def __str__(self):
            #     return f"x: {self.x} y {self.y} d {self.direction}"

        def __repr__(self):
            return f"x: {self.x} y {self.y} d {self.direction}"


def attemptPuzzle(x = 0,y = 0):
    p = Puzzle(x,y)
    print(f"Looking for solution: for ({x}, {y})" )
    try:
        solution = p.solve()
        print(solution.show_moves())

    except Puzzle.DeadEnd:
        print("no solution found")

def main():
    for r in range(5):
        for c in range(5 - r):
            attemptPuzzle(r,c)
            break
        break



if __name__ == '__main__':
    main()
