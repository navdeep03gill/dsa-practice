# need to get all adjacent neighbours of an island
from typing import List

class Solution:
    def restoreGraph(self, grid: List[List[str]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '#':
                    grid[i][j] = '1'
        return
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS(grid, i, j)
                    count += 1
        return count
    def DFS(self, grid, i, j):
        if i < 0 or j < 0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.DFS(grid, i-1, j)
        self.DFS(grid, i+1, j)
        self.DFS(grid, i, j-1)
        self.DFS(grid, i, j+1)
        
testGraph1 = [  ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
testGraph2 = [  ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]]

numberOfIslands = Solution()
assert(numberOfIslands.numIslands(testGraph1) == 1)
assert(numberOfIslands.numIslands(testGraph2) == 3)
numberOfIslands.restoreGraph(testGraph1)
numberOfIslands.restoreGraph(testGraph2)


res1 = numberOfIslands.numIslands(testGraph1)
print(res1)
res2 = numberOfIslands.numIslands(testGraph2)
print(res2)

# beats a significant number of users with python3


