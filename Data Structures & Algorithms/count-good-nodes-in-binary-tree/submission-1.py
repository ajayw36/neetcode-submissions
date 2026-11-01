# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A node is considered good if the path from the root to the node contains no nodes with a value greater than the node

# For each path, we only need to keep track of the maximum node seen so far, because that's the only information we need to determine whether a node is good

# We can perform a DFS while keeping track of (node, max_val) in our stack

# Every time we pop a node from the stack we update our result is node.val >= max_val

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, -float('inf'))]
        while stack:
            curr, max_val = stack.pop()
            if curr.val >= max_val:
                res += 1
                max_val = curr.val
            if curr.left: stack.append((curr.left, max_val))
            if curr.right: stack.append((curr.right, max_val))

        return res


        