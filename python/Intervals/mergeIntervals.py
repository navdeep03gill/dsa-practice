from typing import List
from collections import deque

class Solution:
    def merge_navdeep(self, intervals: List[List[int]]) -> List[List[int]]:
        #intervals = sorted(intervals, key=lambda x: x[1])
        intervals.sort(key=lambda x: x[1])
        new_stack = [intervals[0]]
        for i in range(1, len(intervals)):
            curr_i = intervals[i]
            while new_stack:
                # merge them
                if curr_i[0] <= new_stack[-1][1]:
                    # apply the change to curr_i
                    curr_i[0] = min(curr_i[0], new_stack[-1][0])
                    curr_i[1] = max(curr_i[1], new_stack[-1][1])
                    new_stack.pop(-1)
                else:
                    break
            new_stack.append(curr_i)
        return new_stack
    """
     second implementation, slightly faster. 
     Sort by starting time. Keep track of prev interval at all times, so you don't need to iterate through already merged intervals
     This prev has the latest merge at all times, since we are merging iteratively, and since the entire input is sorted by 
     start time.
    """
    def merge_sample(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        for inter in intervals[1:]:
            if inter[0] <= prev[1]:
                prev[1] = max(inter[1], prev[1])
            else:
                merged.append(prev)
                prev = inter
        merged.append(prev)
        return merged
    
        
def main():
    soln = Solution()
    intervals1 = [[1,3],[3,5],[2,10],[8,9]]
    res_intervals = soln.merge_sample(intervals1)
    print(res_intervals)


    return 0

if __name__ == "__main__":
    main()