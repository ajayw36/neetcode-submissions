# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = []
        stack.append([root, root.val])
        res = 0

        while stack:
            node, greatest_val = stack.pop()
            if node.val >= greatest_val:
                res += 1
                greatest_val = node.val
            if node.left:
                stack.append([node.left, greatest_val])
            if node.right:
                stack.append([node.right, greatest_val])
            
        return res
    
        