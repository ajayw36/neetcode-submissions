class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        vector<int> res;
        for(int num : nums){
            counts[num] += 1;
        }

        vector<pair<int,int>> arr;
        for(const auto& p : counts) {
            arr.push_back({p.second, p.first});
        }

        sort(arr.begin(), arr.end());

        for (int i = arr.size() - 1; k > 0; --k) {
            res.push_back(arr[i].second);
            --i;
        }

        return res;

    }
};
