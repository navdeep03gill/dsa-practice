class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        newS = ""
        for i in range(0, len(s)):
            newVal = s[i]
            if ord("A") <= ord(s[i]) <= ord("Z"):
                newVal = chr(ord(s[i]) + 32)

            elif not (
                ord("a") <= ord(s[i]) <= ord("z") or ord("0") <= ord(s[i]) <= ord("9")
            ):
                continue
            newS += newVal
        left = 0
        right = len(newS) - 1
        while left <= right:
            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1
        return True
