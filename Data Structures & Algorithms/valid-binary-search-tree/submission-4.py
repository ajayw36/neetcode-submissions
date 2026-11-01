# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# In order to check for a valid binary search tree, we need to make sure a few things. First, the node and both its children satisfy the BST property. Second that every node in the left subtree and every node in the right subtree satisfies the BST property with relation to the root. Finally, that every child node is also a valid BST

# This naturally leads to a bottom up DFS approach. An empty tree is a valid BST, so is a tree with one node. What we want to return is True/False whether a tree is a valid BST, but also the min and max value in that tree, as that will help us with the trees above. We will return (is_valid, min_val, max_val)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (True, float('inf'), -float('inf'))
            left, left_min, left_max = dfs(root.left)
            right, right_min, right_max = dfs(root.right)
            min_val = min(left_min, root.val)
            max_val = max(right_max, root.val)
            if left_max < root.val and right_min > root.val and left and right:
                return (True, min_val, max_val)
            else:
                return (False, min_val, max_val)
        return dfs(root)[0]

            