# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# max diameter going through the root of any tree is max depth of the left subtree + max depth of the right subtree

# iterate through every node in the tree, for each node find the max diameter going through that node (by finding the max depth of the left and right subtrees), and update the result

# however, this approach would require a lot of repeated work. instead let's precompute the max depth of each node and use that in our algorithm

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        max_depth = {}
        max_depth[None] = 0
        
        def dfs(curr):
            if not curr: return 0
            if curr in max_depth: return max_depth[curr]
            max_depth[curr] = 1 + max(dfs(curr.left), dfs(curr.right))
            return max_depth[curr]
        
        dfs(root)

        res = 0
        def max_diameter_search(curr):
            nonlocal res
            if not curr: return 0
            
            res = max(res, max_depth[curr.left] + max_depth[curr.right])

            max_diameter_search(curr.left)
            max_diameter_search(curr.right)
        
        max_diameter_search(root)
        return res

        




        