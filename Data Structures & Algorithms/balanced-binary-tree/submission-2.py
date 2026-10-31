# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Brute force solution: iterate through each node, compute the max depth of the left and right subtrees, and return false if they differ by more than one, otherwise return true

# An optimization on that would be to use a recursive DFS to compute the max depths of each node, store them in a map, and then iterate through the nodes while checking the precomputed left and right subtree depths

# This can be further optimized from two passes into one pass by performing the check within the DFS itself. In the DFS function, you check that the left and right subtrees don't differ by more than one, then you return the max depth

# Now a final optimization is to use a sentinel value to immediately terminate after an unbalanced tree

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
    
        def dfs(root):
            if not root: return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if left == -1 or right == -1: return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1
        
        return dfs(root) != -1

        