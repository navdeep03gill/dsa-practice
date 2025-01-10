from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            res = max(res, len(sub))
        return res
