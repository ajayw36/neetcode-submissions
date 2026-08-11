class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        vector<int> res;
        for(int num : nums){
            counts[num] += 1;
        }

        priority_queue<pair<int,int>> max_heap;
        for (const auto& pair : counts){
            max_heap.push({pair.second, pair.first});
        }

        for (; k > 0; --k){
            res.push_back(max_heap.top().second);
            max_heap.pop();
        }

        return res;
    }
};
