import sys
from collections import namedtuple
class Puzzle:
    rows = 5
    num_pegs = 15

    def __init__(self, missing):

        if missing is None:
            self.missing = 0
        else:
            self.missing = missing

        self.jumps = []
        self.init_board()
        self.calc_possible_jumps()
        self.pegs = set(range(Puzzle.num_pegs))
        self.pegs_copy = set(range(Puzzle.num_pegs))

        self.pegs.remove(self.missing)
        self.won = False

    def init_board(self):
        """Create Board like this
        0
        1  2
        3  4  5
        6  7  8  9
        10 11 12 13 14
        """

        # counting backward 14 - 0
        i = Puzzle.num_pegs - 1

        self.board = []


        for row in range(Puzzle.rows):
            self.board.append([])
            vals = []
            for col in range(Puzzle.rows - row):
                vals.append(i)
                i -= 1
            vals.reverse()
            self.board[row] = vals

        self.board = list(reversed(self.board))

    def calc_possible_jumps(self):
        """ Calculate all possible jumps from the board """
        self.possible_jumps = []

        for i,row in enumerate(self.board):
            for j, col in enumerate(row):
                from_ = self.board[i][j]
                if i + 2 < len(self.board):
                    jumping = self.board[i+1]
                    to = self.board[i+2]
                    for k  in [0,2]:
                        self.possible_jumps.append((from_, jumping[j+k//2],to[j+k]))

                if j + 2 < len(row):
                    self.possible_jumps.append((from_, self.board[i][j+1], self.board[i][j+2]))

        # every jump can be made in reverse!
        for jump in self.possible_jumps[:]:
            self.possible_jumps.append(tuple(reversed(jump)))

    def can_jump(self,jump):
        return (jump[0] in self.pegs and
                jump[1] in self.pegs and
                jump[2] not in self.pegs)

    @property
    def valid_jumps(self):
        return filter(self.can_jump, self.possible_jumps)

    def make_jump(self, jump):
        self.pegs.remove(jump[0])
        self.pegs.remove(jump[1])
        self.pegs.add(jump[2])
        self.jumps.append(jump)

    def undo(self):
        jump = self.jumps.pop()
        self.pegs.add(jump[0])
        self.pegs.add(jump[1])
        self.pegs.remove(jump[2])

    def solve(self, memory = set()):
        if self.won:
            return True

        for jump in self.valid_jumps:
            self.make_jump(jump)

            # one peg remains, equals solved
            if len(self.pegs) == 1:
                # cut out early
                raise Exception("Won")
                self.won = True

            # solve it with jump made
            self.solve()
            # bad jump, undo and try another
            self.undo()

        if str(self.jumps) in memory:
            print('goo',self.jumps)
        memory.add(str(self.jumps))

        return False

    def replay(self):
        self.pegs = self.pegs_copy
        self.pegs.remove(self.missing)
        for jump in self.jumps:
            self.make_jump(jump)
            print(self)


    def pegAsStr(self, pegNum):
        return "x " if pegNum in self.pegs else "- "

    def __str__(self):
        newlineAfter = 1
        vals = 0
        s = "\n"
        for peg_num in range(Puzzle.num_pegs):
            vals += 1
            s += self.pegAsStr(peg_num)

            if vals >= newlineAfter:
                newlineAfter += 1
                vals = 0
                s += "\n"

        return s

def main(args):
    puzzle = Puzzle(int(args))
    try:
        print(puzzle)
        puzzle.solve()
    except Exception as err:
        print(f'Won in {len(puzzle.jumps)} jumps.')
        try:
            puzzle.replay()
        except:
            pass


if __name__ == "__main__":
    main(sys.argv[1])
