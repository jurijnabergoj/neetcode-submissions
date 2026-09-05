# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def heightOfBinaryTree(node):
            if not node: return 0
            return 1 + max(heightOfBinaryTree(node.left), heightOfBinaryTree(node.right))

        if not root: return 0

        subtree_sum = heightOfBinaryTree(root.left) + heightOfBinaryTree(root.right)
        
        return max(subtree_sum, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))
        
        

