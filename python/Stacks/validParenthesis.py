class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = []
        j = 0
        for i in range(len(s)):
            curr = s[i]
            if curr == '(' or curr == '{' or curr == '[':
                parenStack.append(curr)
                j += 1
            else:
                if len(parenStack) == 0:
                    return False
                start = parenStack.pop()
                j -= 1

                if (curr == ')' and start == '(') or (curr == ']' and start == '[') or (curr == '}' and start == '{'):
                    continue
                else:
                    return False
        if len(parenStack) > 0:
            return False
        return True

