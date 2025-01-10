from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        mininum = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            mid = nums[m]
            if mininum < mid:
                l = m+1
            elif mininum > mid:
                r = m-1
                mininum = mid
        return mininum
        
        

