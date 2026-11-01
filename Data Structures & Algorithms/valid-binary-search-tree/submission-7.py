# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder traversal

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        prev = None

        def inorder(root):
            if not root: return

            inorder(root.left)

            curr = root.val
            nonlocal prev, valid
            if prev is not None:
                if curr <= prev: valid = False

            prev = curr

            inorder(root.right)
        inorder(root)
        return valid