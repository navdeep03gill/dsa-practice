from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elms = set()
        for i in nums:
            elms.add(i)
        maxRet = []
        for i in elms:
            if i - 1 in elms:
                continue
            currSeq = [i]
            rightSeq = i + 1
            while rightSeq in elms:
                currSeq.append(rightSeq)
                rightSeq += 1
            if len(currSeq) > len(maxRet):
                maxRet = currSeq
        return len(maxRet)
