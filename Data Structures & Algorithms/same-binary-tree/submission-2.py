# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        p_stack = [p]
        q_stack = [q]
        
        while p_stack and q_stack:
            p_curr = p_stack.pop()
            q_curr = q_stack.pop()

            if p_curr is None and q_curr is None:
                continue

            if (p_curr is None or q_curr is None) or p_curr.val != q_curr.val:
                return False                

            p_stack.append(p_curr.left)
            p_stack.append(p_curr.right)
            q_stack.append(q_curr.left)
            q_stack.append(q_curr.right)
        
        return True