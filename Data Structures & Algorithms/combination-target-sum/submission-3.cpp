class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> curr;
        search(res, nums, curr, 0, target, 0);
        return res;
    }

    void search(vector<vector<int>>& res, vector<int>& nums, vector<int>& curr, int curr_sum, int target, int i) {
        if (curr_sum == target) {
            res.push_back(curr);
            return;
        }
        else if (curr_sum > target) {
            return;
        }
        if (i == nums.size()) return;
        
        curr_sum += nums[i];
        curr.push_back(nums[i]);
        search(res, nums, curr, curr_sum, target, i);

        curr_sum -= nums[i];
        curr.pop_back();
        search(res, nums, curr, curr_sum, target, i + 1);
    }
};
