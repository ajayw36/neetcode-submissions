# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We are given access to p, q, and root. We can use these three values to figure out where in the binary tree we are. If p and q are both less than root, then we know we're in the left subtree of root, if one is less and one is greater, we can immediately return root.

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val <= root.val and q.val >= root.val: return root
        if p.val >= root.val and q.val <= root.val: return root

        if p.val <= root.val and q.val <= root.val: return self.lowestCommonAncestor(root.left, p, q)
        else: return self.lowestCommonAncestor(root.right, p, q)

        