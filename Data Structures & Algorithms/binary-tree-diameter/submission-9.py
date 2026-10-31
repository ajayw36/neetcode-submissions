# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Optimize further to update result within the initial pass

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0

        def dfs(curr):
            nonlocal res
            if not curr: return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            res = max(res, left + right)
            return max(left, right) + 1
        
        dfs(root)
        return res
            