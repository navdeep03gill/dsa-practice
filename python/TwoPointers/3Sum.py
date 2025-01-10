from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        toret = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                target = a + nums[left] + nums[right]
                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                else:
                    toret.append([a, nums[left], nums[right]])
                    left += 1
                    while (nums[left] == nums[left - 1]) and (left < right):
                        left += 1
        return toret
