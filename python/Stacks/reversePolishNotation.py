class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if (c == '+'):
                right = stack.pop()
                left = stack.pop()
                res = int(left) + int(right)
                stack.append(res)

            elif (c == '-'):
                right = stack.pop()
                left = stack.pop()
                res = int(left) - int(right)
                stack.append(res)
            elif (c == '*'):
                right = stack.pop()
                left = stack.pop()
                res = int(left) * int(right)
                stack.append(res)
            elif (c == '/'):
                right = stack.pop()
                left = stack.pop()
                res = int(left / right)
                stack.append(res)
            
            else:
                stack.append(int(c))
            
        return stack[0]


