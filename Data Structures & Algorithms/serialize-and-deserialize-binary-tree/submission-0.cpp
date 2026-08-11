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

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string res = "";
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* n = q.front();
            q.pop();
            if (n == nullptr) {
                res += "n,";
            }
            else {
                res += to_string(n->val) + ",";
                q.push(n->left);
                q.push(n->right);
            }
        }
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        string val;
        getline(ss, val, ',');
        if (val == "n") return nullptr;
        TreeNode* root = new TreeNode(stoi(val));
        queue<TreeNode*> q;
        q.push(root);

        while (getline(ss, val, ',')) {
            TreeNode* n = q.front();
            q.pop();
            if (val != "n") {
                n->left = new TreeNode(stoi(val));
                q.push(n->left);
            }
            getline(ss, val, ',');
            if (val != "n") {
                n->right = new TreeNode(stoi(val));
                q.push(n->right);
            }
        }
        return root;
    }

};
