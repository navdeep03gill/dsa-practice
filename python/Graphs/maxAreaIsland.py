from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 0
                    area = self.dfsvisit(grid, i, j, area)
                    if area > maxArea:
                        maxArea = area

        return maxArea
    def dfsvisit(self, grid, i, j, area):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return area
        grid[i][j] = 2
        area += 1
        area = self.dfsvisit(grid, i-1, j, area)
        area = self.dfsvisit(grid, i+1, j, area)
        area = self.dfsvisit(grid, i, j-1, area)
        area = self.dfsvisit(grid, i, j+1, area)
        return area

input= [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

soln = Solution()
area = soln.maxAreaOfIsland(input)
print(area)
                

