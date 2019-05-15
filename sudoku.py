class SudokuSolver():
    def __init__(self, puzzle):
        inp = puzzle.strip().split()
        inp = [int(c) for c in inp]
        import math
        dim = int(math.sqrt(len(inp)))
        hdim = int(math.sqrt(dim))

        grid = []
        for i in range(0,len(inp),dim):
            grid.append(inp[i:i+dim])

        # set important parameters
        self.nums = set(range(1, dim+1))
        self.cells = set(range(1, dim*dim+1))
        self.dim = dim
        self.hdim = hdim
        self.grid = grid
        
    def create_helper_arrays(self):
        import numpy as np
        hdim = self.hdim
        dim = self.dim
        grid= self.grid

        mapping = np.zeros((hdim,hdim))
        orig_mapping = mapping + 1
        for i in range(hdim-1): mapping = np.hstack((mapping, orig_mapping+i))
        orig_mapping = mapping + hdim
        for i in range(hdim-1):
            mapping = np.vstack((mapping, orig_mapping+i*hdim))
        mapping = mapping.astype(int).tolist()

        rownums = []
        colnums = []
        for i in range(dim):
            rownums.append({grid[i][col] for col in range(dim)})
            colnums.append({grid[row][i] for row in range(dim)})

        boxnums = {}
        for i in range(dim): boxnums[i] = set()
        for row in range(dim):
            for col in range(dim):
                boxnums[mapping[row][col]].add(grid[row][col])

        self.mapping = mapping
        self.rownums = rownums
        self.colnums = colnums
        self.boxnums = boxnums

    
    def get_row(self, cell):
        return (cell-1) // self.dim

    def get_col(self, cell):
        return (cell-1) % self.dim 

    def get_box(self, cell):
        row = self.get_row(cell)
        col = self.get_col(cell)
        return self.mapping[row][col]

    def allowed(self, cell):
        row = self.get_row(cell)
        col = self.get_col(cell)
        if self.grid[row][col] != 0: return {self.grid[row][col]}
        box = self.get_box(cell)
        return self.nums - self.rownums[row].union(self.colnums[col]).union(self.boxnums[box])

    def cell_to_rel_col_nbrs(self, cell):
        col = self.get_col(cell)
        return [c  for c in range(1,cell) if self.get_col(c) == col]

    def cell_to_rel_row_nbrs(self, cell):
        row = self.get_row(cell)
        return [c  for c in range(1,cell) if self.get_row(c) == row]

    def cell_to_rel_box_nbrs(self, cell):
        box = self.get_box(cell)
        return [c for c in range(1,cell) if self.get_box(c) == box]

    def cell_to_rel_nbrs(self, cell):
        ''' cell to relevant neighbors'''
        return set(self.cell_to_rel_col_nbrs(cell) + 
                   self.cell_to_rel_row_nbrs(cell) + 
                   self.cell_to_rel_box_nbrs(cell))

    def gen_cell_exp(self, cell): 
        allowed_nums = self.allowed(cell)
        result = f'for x{cell} in {allowed_nums}' 
        nbrs = self.cell_to_rel_nbrs(cell)
        if len(nbrs) != 0:
            result = result + ' - {'+ ','.join([f'x{i}' for i in nbrs]) + '} '
        return result 

    def gen_full_exp(self):
        sol = '((' + ','.join([f'x{cell}' for cell in self.cells]) + ') '
        sol = sol + ' '.join([self.gen_cell_exp(cell) for cell in self.cells])
        sol = sol + ')'
        return sol

    def solve(self):
        self.create_helper_arrays()
        soln = next(eval(self.gen_full_exp()))
        for i in range(self.dim):
            print(soln[i*self.dim:(i+1)*self.dim])

            
if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    puzzle = open(filename).read()
    SudokuSolver(puzzle).solve()



