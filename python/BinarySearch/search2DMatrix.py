from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nSize = len(matrix[0])
        mSize = len(matrix)
        mleft = 0
        mright = mSize - 1
        while mleft <= mright:
            mMid = (mleft + mright) // 2

            if matrix[mMid][0] > target:
                mright = mMid - 1
                continue
            elif matrix[mMid][nSize-1] < target:
                mleft = mMid + 1
                continue
            else:
                arr = matrix[mMid]
                left = 0
                right = nSize - 1
                while left <= right:
                    mid = (left + right) // 2
                    if (arr[mid] == target):
                        return True
                    elif arr[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                break
        return False
            
