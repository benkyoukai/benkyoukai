import sys

def pr(matrix):
    for row in matrix:
        print row

class Sudoku:
    def solve(self, data):
        self.data  = data
        self.nums = set([1,2,3,4,5,6,7,8,9])
        self.setup()
        self.run()

        return self.data

    # Setup
    #
    #   - fixed
    #   - tried
    #   - columns
    #   - rows
    #   - boxes
    def setup(self):
        self.fixed = set([])
        self.tried = {}
        self.cols = []
        self.boxes = []
        self.rows = []

        # init columns
        # init rows
        # inti boxes
        for i in range(0, 9):
            self.cols.append(set([]))
            self.rows.append(set([]))
            self.boxes.append(set([]))

        for y in range(9):
            row = self.data[y]
            for x in range(9):
                if not row[x] == ".":
                    self.fixed.add((x,y))
                    self.colset(x, y, row[x])
                    self.rowset(x, y, row[x])
                    self.boxset(x, y, row[x])
                else:
                    self.tried[(x,y)] = set([])

    # set & unset
    def boxindex(self, x, y):
        return (y / 3) * 3 + x / 3

    def rowset(self, x, y, v):
        self.rows[y].add(v)

    def colset(self, x, y, v):
        self.cols[x].add(v)

    def boxset(self, x, y, v):
        index = self.boxindex(x, y)
        self.boxes[index].add(v)

    def rowunset(self, x, y, v):
        self.rows[y].remove(v)

    def colunset(self, x, y, v):
        self.cols[x].remove(v)

    def boxunset(self, x, y, v):
        index = self.boxindex(x, y)
        self.boxes[index].remove(v)

    def set(self, x, y, v):
        self.data[y][x] = v
        self.tried[(x,y)].add(v)
        self.rowset(x, y, v)
        self.colset(x, y, v)
        self.boxset(x, y, v)

    def unset(self, x, y):
        v = self.data[y][x]
        self.data[y][x] = "."
        self.rowunset(x, y, v)
        self.colunset(x, y, v)
        self.boxunset(x, y, v)

    # getter
    def row(self, x, y):
        return self.rows[y]

    def col(self, x, y):
        return self.cols[x]

    def box(self, x, y):
        index = self.boxindex(x, y)
        return self.boxes[index]

    # value for current set
    def available(self, x, y):
        tmp = self.nums - (self.row(x, y) | self.col(x, y) | self.box(x, y) | self.tried[(x,y)])
        return tmp

    def valid(self, x, y):
        tmp = self.available(x, y)
        if len(tmp) > 0:
            return next(iter(tmp))

    # cells
    def nextcell(self, x, y):
        while True:
            if x < 8:
                x += 1
            else:
                y += 1
                x = 0

            if (x, y) not in self.fixed:
                break

        return (x, y)

    def prevcell(self, x, y):
        while True:
            if x > 0:
                x -= 1
            else:
                y -= 1
                x = 8

            if (x, y) not in self.fixed:
                break

        return (x, y)

    def validcell(self, x, y):
        return 0 <= y < 9

    # Logic
    def run(self):
        x, y = 0, 0
        if (x, y) in self.fixed:
            x, y = self.nextcell(x, y)

        while self.validcell(x, y):
            value = self.valid(x, y)
            if not value:
                self.tried[(x, y)].clear()
                x, y = self.prevcell(x,y)
                self.unset(x, y)
                continue

            self.set(x, y, value)
            x, y = self.nextcell(x, y)


if __name__ == "__main__":
    matrix = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9],
    ]

    for row in matrix:
        for i in range(9):
            if row[i] == 0:
                row[i] = "."

    # pr(matrix)
    print
    solve = Sudoku()
    solve.solve(matrix)
    pr(matrix)
    print "--------------------------------------------"

    matrix = [
        ['.', '.', '9', '7', '4', '8', '.', '.', '.'],
        ['7', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '1', '.', '9', '.', '.', '.'],
        ['.', '.', '7', '.', '.', '.', '2', '4', '.'],
        ['.', '6', '4', '.', '1', '.', '5', '9', '.'],
        ['.', '9', '8', '.', '.', '.', '3', '.', '.'],
        ['.', '.', '.', '8', '.', '3', '.', '2', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '2', '7', '5', '9', '.', '.']
    ]

    for row in matrix:
        for i in range(9):
            if not row[i] == ".":
                row[i] = int(row[i])
    solve.solve(matrix)
    pr(matrix)
