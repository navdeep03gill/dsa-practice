from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else: return -1
        l = 0
        r = len(nums) - 1
        while (l <= r):
            m = (r+l) // 2
            print(l, r, m)
            left = nums[l]
            right = nums[r]
            mid = nums[m]
            if mid == target: return m
            # left sorted
            if left <= mid:
                if target > mid or target < left:
                    l = m + 1
                else:
                    r = m - 1
            # right sorted 
            else:
                if target < mid or target > right:
                    r = m - 1
                else:
                    l = m + 1
        return -1

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        def indexSearch(nums: List[int], idx: int):
            if (len(nums) == 1):
                return idx if nums[0] == target else -1
            
            if (len(nums) == 2):
                if nums[0] == target:
                    return idx
                if nums[1] == target:
                    return idx + 1
                else: return -1
            
            midIdx = len(nums) // 2
            print(midIdx)
            mid = nums[midIdx]
            if (mid == target):
                return idx + midIdx
            leftSide = nums[0:midIdx]
            rightSide = nums[midIdx:]
            left = indexSearch(leftSide, idx) 
            right = indexSearch(rightSide, idx + midIdx)
            if left != -1:
                return left
            elif right != -1:
                return right
            return -1
        return indexSearch(nums, 0)



class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]: return 0
            return - 1
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = (left + right) // 2
            print(left, mid, right)
            if nums[mid] == target: 
                return mid
            
            # check left side sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right side sorted
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
