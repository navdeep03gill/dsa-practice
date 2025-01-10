from typing import List

class SolutionAttemptOne:
    def characterReplacement(self, s: str, k: int) -> int:
        currChar = ''
        l = 0
        res = 0
        kCap = k
        r = 0
        while(r < len(s)):
            print(l, r)
            if currChar == '':
                currChar = s[r]
            elif s[r] != currChar:
                if kCap == 0:
                    l += 1
                    r = l
                    currChar = s[l]
                    kCap = k
                else:
                    kCap -= 1
            res = max(res, r - l + 1)
            r += 1
        currChar = ''
        l = len(s) - 1
        r = len(s) - 1
        kCap = k
        while(r >= 0):
            print(l, r)
            if currChar == '':
                currChar = s[r]
            elif s[r] != currChar:
                if kCap == 0:
                    l -= 1
                    r = l
                    currChar = s[l]
                    kCap = k
                else:
                    kCap -= 1
            res = max(res, l - r + 1)
            r -= 1
        return res
            
class SolutionSuccess:
    def characterReplacement(self, s: str, k: int) -> int:
        windowHash = {}
        lCount = 0
        res = 0
        l = 0
        r = 0
        while (r < len(s)):
            if s[r] not in windowHash:
                windowHash[s[r]] = 1
            else:
                windowHash[s[r]] += 1
            
            for val in windowHash.values():
                lCount = max(lCount, val)

            kCap = (r - l + 1) - lCount
            
            if kCap <= k:
                res = max(res, (r - l + 1))
            
            else:
                windowHash[s[l]] -= 1
                windowHash[s[r]] -= 1
                l += 1
                r -= 1
            r += 1
        return res

class SolutionSuccess2:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
