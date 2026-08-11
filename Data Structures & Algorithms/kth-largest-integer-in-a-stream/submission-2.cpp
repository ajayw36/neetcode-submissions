class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> min_heap;
    int k;
public:
    KthLargest(int k, vector<int>& nums) : k(k), min_heap(nums.begin(), nums.end()) {
        while (min_heap.size() > k) {
            min_heap.pop();
        }
    }
    
    int add(int val) {
        min_heap.push(val);
        if (min_heap.size() > k) {
            min_heap.pop();
        }
        return min_heap.top();
    }
};
