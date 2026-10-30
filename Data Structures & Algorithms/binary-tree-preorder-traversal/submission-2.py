# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root
        stack.append(curr)

        # [1]
        # [3, 2, 1]
        # [3, 2] [1]
        # [3, 2]
        # [3, 5, 4][1, 2]

        # curr = stack.pop()
        # stack.append(curr.right)
        # stack.append(curr.left)

        while stack:
            curr = stack.pop()
            if curr: res.append(curr.val)
            if curr and curr.right: stack.append(curr.right) 
            if curr and curr.left: stack.append(curr.left)
        
        return res
            