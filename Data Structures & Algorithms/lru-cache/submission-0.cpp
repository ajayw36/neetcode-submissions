class LRUCache {
private:
    class Node {
        friend class LRUCache;

        int key;
        int val;
        Node* next;
        Node* prev;

        Node(int key, int val) : key(key), val(val), next(nullptr), prev(nullptr) {}
    };

    unordered_map<int, Node*> cache;
    int capacity;
    Node* left;
    Node* right;

    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void insert(Node* node) {
        Node* prev = right->prev;
        prev->next = node;
        node->prev = prev;
        node->next = right;
        right->prev = node;
    }

public:
    LRUCache(int capacity) : capacity(capacity), left(new Node(0,0)), right(new Node(0,0)) {
        left->next = right;
        right->prev = left;
    }
    
    int get(int key) {
        // Get node and put it on right
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        Node* node = cache[key];
        remove(node);
        insert(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            remove(cache[key]);
        }
        Node* node = new Node(key, value);
        cache[key] = node;
        insert(node);

        if (cache.size() > capacity) {
            Node* lru = left->next;
            remove(lru);
            cache.erase(lru->key);
            delete lru;
        }
    }
};
