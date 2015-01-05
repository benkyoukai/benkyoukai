class NQueens:
    def solve(self, n):
        self.n = n
        self.row = ["."] * n
        self.nums = set(range(n))
        sols = self.run()

        return map(lambda sol: self.matrix(sol), sols)

    def run(self):
        n = self.n
        sols = [[]]

        for y in range(n):
            newsols = []
            for sol in sols:
                xs = self.xs(y, sol)
                for x in xs:
                    newsols.append(sol + [x])
            sols = newsols
        return sols

    def xs(self, y, sol):
        n = self.n
        fixedx = set([])
        size = len(sol)

        for fy in range(size):
            fx = sol[fy]
            fixedx.add(fx)
            dy = y - fy

            if fx + dy < n:
                fixedx.add(fx + dy)
            if fx - dy >= 0:
                fixedx.add(fx - dy)

        return self.nums - fixedx

    def matrix(self, arr):
        m = []
        for i in arr:
            row = list(self.row)
            row[i] = "Q"
            m.append("".join(row))
        return m

if __name__ == "__main__":
    def pp(sol):
        for row in sol:
            print row

    solve = NQueens()
    sols = solve.solve(9)
    for sol in sols:
        pp(sol)
        print
