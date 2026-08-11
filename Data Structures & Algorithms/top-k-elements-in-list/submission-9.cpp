class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        vector<vector<int>> freq(nums.size() + 1);

        for (int num : nums) {
            counts[num] += 1;
        }

        for (auto& pair : counts) {
            freq[pair.second].push_back(pair.first);
        }

        vector<int> res;

        for (int i = freq.size() - 1; k > 0; --i) {
            for(int j = 0; j < freq[i].size(); ++j) {
                res.push_back(freq[i][j]);
                --k;
            }
        }

        return res;
    }
};
