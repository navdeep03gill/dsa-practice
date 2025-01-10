class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        def expandFromCenter(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]
        
        max_str = s[0]
        for i in range(len(s) - 1):
            # odd case
            odd_str = expandFromCenter(i, i)
            even_str = expandFromCenter(i, i+1)
            if len(odd_str) > len(max_str):
                max_str = odd_str
            if len(even_str) > len(max_str):
                max_str = even_str
        return max_str
        #Brute Force
        """
        if len(s) <= 1:
            return s
        max_len = 1
        max_str = s[0]
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if (j-i+1) > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = (j-i+1)
                    max_str = s[i:j+1]
        return max_str
        """

soln = Solution()
exString = "babad"
res = soln.longestPalindrome(exString)
print(exString, res)
