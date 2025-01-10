from typing import List

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        water = 0
        land = 1
        perimeter = 0
        for i in range(0, len(grid)):
            upBound = (i == 0)
            lowBound = (i == (len(grid) - 1))
            for j in range(0, len(grid[i])):
                leftBound = (j == 0)
                rightBound = (j == (len(grid[i])-1))
                if (grid[i][j] == land):
                    # up case
                    if (upBound):
                        perimeter += 1
                    elif( i > 0 and grid[i-1][j] == water):
                        perimeter += 1
                    # left case
                    if (leftBound):
                        perimeter += 1
                    elif (j > 0 and grid[i][j-1] == water):
                        perimeter += 1
                    # right case
                    if (rightBound):
                        perimeter += 1
                    elif (j < len(grid[i])-1 and grid[i][j+1] == water):
                        perimeter += 1
                    # down case
                    if (lowBound):
                        perimeter += 1
                    elif (i < len(grid) - 1 and grid[i+1][j] == water):
                        perimeter += 1
        return perimeter
soln = Solution()
perim = soln.islandPerimeter(grid)
print(perim)
