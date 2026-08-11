class PrefixTree {
public:
    struct TrieNode {
        bool is_end = false;
        vector<TrieNode*> children;

        TrieNode() {
            children.resize(26);
        }
    };

    TrieNode* root;


    PrefixTree() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* curr = root;
        for (char ch : word) {
            char c = ch - 'a';
            if (!curr->children[c]) {
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->is_end = true;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        for (char ch : word) {
            char c = ch - 'a';
            if (!curr->children[c]) {
                return false;
            }
            curr = curr->children[c];
        }
        return curr->is_end;
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char ch : prefix) {
            char c = ch - 'a';
            if (!curr->children[c]) {
                return false;
            }
            curr = curr->children[c];
        }
        return true;
    }
};
