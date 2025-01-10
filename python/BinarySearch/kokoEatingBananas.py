from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (r + l) // 2
            totalTime = 0
            for p in piles:
                totalTime += ceil(p / mid)
            if totalTime <= h:
                res = min(res, mid)
                r = mid - 1
            elif totalTime > h:
                l = mid + 1
        return res
soln = Solution()
print(soln.minEatingSpeed([3, 6, 7, 11], 8))
