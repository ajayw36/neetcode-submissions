class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;
        search(res, nums, subset, 0);
        return res;
    }

    void search(vector<vector<int>>& res, vector<int>& nums, vector<int>& subset, int i) {
        if (i >= nums.size()) {
            res.push_back(subset);
            return;
        }
        subset.push_back(nums[i]);
        search(res, nums, subset, i+1);
        subset.pop_back();
        search(res, nums, subset, i+1);
    }
};
