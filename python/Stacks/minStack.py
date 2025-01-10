from typing import List
import collections


class MinStack:

    def __init__(self):
        self.stack = []
        self.stackDesc = []
        return

    def push(self, val: int) -> None:
        if len(self.stackDesc) == 0 or self.stackDesc[len(self.stackDesc)-1] >= val:
            self.stackDesc.append(val)
        self.stack.append(val)
        return       

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        toret = self.stack[len(self.stack)-1]
        self.stack.pop(len(self.stack)-1)
        if toret == self.stackDesc[len(self.stackDesc)-1]:
            self.stackDesc.pop(len(self.stackDesc)-1)
        return

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        toret = self.stack[len(self.stack)-1]
        return toret

    def getMin(self) -> int:
        if len(self.stackDesc) == 0: return
        return self.stackDesc[len(self.stackDesc)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

soln = MinStack()
print(soln.push(2))
print(soln.push(0))
print(soln.push(3))
print(soln.push(0))
print(soln.getMin())
print(soln.pop())
print(soln.getMin())
print(soln.pop())
print(soln.getMin())
print(soln.pop())
print(soln.getMin())


