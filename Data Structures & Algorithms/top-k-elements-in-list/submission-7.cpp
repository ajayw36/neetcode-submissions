class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num] += 1;
        }

        priority_queue<pair<int, int>> max_heap;

        for (auto& pair : counts) {
            max_heap.push({pair.second, pair.first});
        }

        vector<int> res;

        while (k > 0) {
            res.push_back(max_heap.top().second);
            max_heap.pop();
            --k;
        }

        return res;
    }
};
