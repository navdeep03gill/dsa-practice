from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        toret = []
        def dfs(left, right, s):
            if len(s) == n*2:
                toret.append(s)
                return
            if left < n:
                dfs(left+1, right, s + '(')
            if right < left:
                dfs(left, right+1, s + ')')
        dfs(0, 0, "")
        return toret

    def generateParenthesisStack(self, n:int) -> List[str]:
        # only add open parenthesis if open < n
        # only add closing parenthesis if closed < open
        # valid IIF open==closed==n
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res

            
            




