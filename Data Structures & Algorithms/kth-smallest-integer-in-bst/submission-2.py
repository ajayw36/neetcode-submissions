# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Since we have a binary search tree, an easy way to get the kth smallest integer would just be to perform an inorder traversal. This would give us all the nodes in increasing order, where we would have O(1) access to the kth smallest. The time and space complexity of this would be O(n), where n is the number of nodes in the tree

# Would you like me to talk through some more solutions first or should I go ahead and implement that?

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def inorder(root):
            if not root: return None
            
            nonlocal count
            

            left = inorder(root.left)
            if left is not None: return left

            count += 1

            if count == k:
                return root.val

            right = inorder(root.right)
            if right is not None: return right
        
        return inorder(root)

