from typing import List,Optional
import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def buildTree(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    q = [root]
    i = 1
    while i < len(nums):
        curr = q.pop(0)
        if i < len(nums):
            curr.left = TreeNode(nums[i])
            q.append(curr.left)
            i += 1
        if i < len(nums):
            curr.right = TreeNode(nums[i])
            q.append(curr.right)
            i += 1
    return root
 
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)


class Solution:
    def helper(self, root, fork):
        if root is None:
            return float("-inf")
        
        leftPathLen = self.helper(root.left, fork) # gives biggest single path up till
        rightPathLen = self.helper(root.right, fork)
        newFork = root.val
        if leftPathLen != float("-inf"):
            newFork += leftPathLen
        if rightPathLen != float("-inf"):
            newFork += rightPathLen
 
        if fork[-1] < max(newFork, root.val, leftPathLen, rightPathLen):
            fork[-1] = max(newFork, root.val, leftPathLen, rightPathLen)

        return max(root.val, root.val + leftPathLen, root.val + rightPathLen)
        
    def maxPathSumOld(self, root: Optional[TreeNode]) -> int:
        fork = [float("-inf")]
        maxSinglePath = self.helper(root, fork)
        if not fork:
            return maxSinglePath
        return max(maxSinglePath, fork[-1])
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        fork = [float("-inf")]
        def dfs(root):
            if root is None:
                return 0
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            fork[0] = max(fork[0], root.val + leftMax + rightMax)

            return max(root.val + leftMax, root.val + rightMax)
        rootMax = dfs(root)
        return max(fork[0], rootMax)

def main():
    nodes = [-10,9,20,3,4,15,7,1,2,1,3,6]
    root = buildTree(nodes)
    printTree(root)
    print()
    soln = Solution()
    maxSum = soln.maxPathSum(root)
    print(maxSum)

if __name__ == "__main__":
    main()
    