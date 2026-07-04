# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0
        stack = []
        stack.append((root, 1))
        while stack:
            curr = stack.pop()
            res = max(res, curr[1])
            if curr[0].left:
                stack.append((curr[0].left, curr[1] + 1))
            if curr[0].right:
                stack.append((curr[0].right, curr[1] + 1))
        return res
