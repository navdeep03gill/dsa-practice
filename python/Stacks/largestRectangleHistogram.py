from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # base case
        stack = [] # pair: (index, height)
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        # still might be entries in the stack left
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

sampleInput = [2,1,5,6,2,3]
soln = Solution()
print(soln.largestRectangleArea(sampleInput))

