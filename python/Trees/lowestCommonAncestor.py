# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left 
            else:
                return root
                
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

def main():
    soln = Solution()
    inp = [5,3,8,1,4,7,9,None,2]
    root = buildTree([5,3,8,1,4,7,9,None,2])
    p = TreeNode(4)
    q = TreeNode(2)
    lca = soln.lowestCommonAncestor(root, p, q)
    print(lca.val)


if __name__ == "__main__":
    main()