# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        st = [root]
        mp = {None: 0} # mapping node to it's height
        
        while st:
            node = st[-1]
            if node.left and node.left not in mp:
                st.append(node.left)
            elif node.right and node.right not in mp:
                st.append(node.right)
            else:
                node = st.pop()
                lh = mp[node.left]
                rh = mp[node.right]

                if abs(lh - rh) > 1:
                    return False
                mp[node] = 1 + max(lh, rh)
        return True
