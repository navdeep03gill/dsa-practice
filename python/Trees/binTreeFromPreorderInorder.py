from typing import List, Optional

# Given two integer arrays preorder and inorder where preorder is the preorder traversal 
# of a binary tree and inorder is the inorder traversal of the same tree, 
# construct and return the binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        VAL_TO_INORDER_IDX = {inorder[i]: i for i in range(len(inorder))}
        
        def buildTreePartition(preorder, inorder_start, inorder_end):
            if not preorder or inorder_start < 0 or inorder_end > len(inorder):
                return None
            root_val = preorder[0]
            root_inorder_idx = VAL_TO_INORDER_IDX[root_val]
            if root_inorder_idx > inorder_end or root_inorder_idx < inorder_start:
                return None
            
            root = TreeNode(preorder.pop(0))
            root.left = buildTreePartition(preorder, inorder_start, root_inorder_idx - 1)
            root.right = buildTreePartition(preorder, root_inorder_idx + 1, inorder_end)

            return root
        return buildTreePartition(preorder, 0, len(inorder) - 1)
    
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            self.printTree(node.left, level + 1)
            



def main():
    print("Hello World!")
    soln = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = soln.buildTree(preorder, inorder)
    soln.printTree(root)


if __name__ == "__main__":
    main()
