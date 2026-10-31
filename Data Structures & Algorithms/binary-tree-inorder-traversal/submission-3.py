# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursively search the left subtree, then append the root, then recursively search the right subtree
        res = []
        def inorder_search(curr):
            if not curr: return
            inorder_search(curr.left)
            res.append(curr.val)
            inorder_search(curr.right)
        inorder_search(root)
        return res