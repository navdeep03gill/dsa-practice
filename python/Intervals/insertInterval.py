from collections import deque
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged1 = []
        added = False
        for inter in intervals:
            if newInterval[0] <= inter[0] and not added:
                merged1.append(newInterval)
                added = True
            merged1.append(inter)
        if not added:
            merged1.append(newInterval)
        
        prev = merged1[0]
        merged2 = []
        for inter in merged1[1:]:
            if inter[0] <= prev[1]:
                prev[0] = min(inter[0], prev[0])
                prev[1] = max(inter[1], prev[1])
            else:
                merged2.append(prev)
                prev = inter
        merged2.append(prev)
        return merged2


def main():
    soln = Solution()
    intervals1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]

    res_intervals = soln.insert(intervals1, newInterval)
    print(res_intervals)
    return 0

if __name__ == '__main__':
    main()

