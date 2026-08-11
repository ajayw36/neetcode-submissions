/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        stack<TreeNode*> stack;
        stack.push(root);

        while (!stack.empty()) {
            TreeNode* curr = stack.top();
            stack.pop();

            if (curr != nullptr) {
                stack.push(curr->left);
                stack.push(curr->right);
                TreeNode* temp = curr->left;
                curr->left = curr->right;
                curr->right = temp;
            }

        }
        
        return root;
    }
};
