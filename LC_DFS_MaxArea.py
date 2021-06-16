class Solution:
    def maxAreaOfIsland(self, grid):
        self.seen = set()
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        area_size_lots = set()
        for row in range(self.rows):
            for column in range(self.columns):
                area_size_lots.add(self.get_island_area(row, column))

        return (max(area_size_lots))

    def get_island_area(self, row, column):
        if (row, column) not in self.seen:
            self.seen.add((row, column))
            if self.grid[row][column] != 0:
                return self.grid[row][column] + \
                       (0 if row - 1 < 0 else self.get_island_area(row - 1, column)) + \
                       (0 if column - 1 < 0 else self.get_island_area(row, column - 1)) + \
                       (0 if row + 1 >= self.rows else self.get_island_area(row + 1, column)) + \
                       (0 if column + 1 >= self.columns else self.get_island_area(row, column + 1))
            else:
                return 0
        else:
            return 0


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0]]

print(Solution().maxAreaOfIsland(grid))