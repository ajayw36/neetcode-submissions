class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> max_heap(stones.begin(), stones.end());
        while (max_heap.size() > 1) {
            int y = max_heap.top();
            max_heap.pop();
            int x = max_heap.top();
            max_heap.pop();
            if (x == y) continue;
            else {
                y = y - x;
                max_heap.push(y);
            }
        }
        if (max_heap.empty()) return 0;
        return max_heap.top();
    }
};
