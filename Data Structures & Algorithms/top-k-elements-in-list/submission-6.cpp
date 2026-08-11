class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num] += 1;
        }

        vector<pair<int, int>> arr;
        for (auto& pair : counts) {
            arr.push_back({pair.second, pair.first});
        }
        sort(arr.begin(), arr.end());

        vector<int> res;

        for (int i = arr.size() - 1; k > 0; --k, --i) {
            res.push_back(arr[i].second);
        }

        return res;

    }
};
