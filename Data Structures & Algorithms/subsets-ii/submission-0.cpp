class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> curr;
        search(nums, res, curr, 0);
        return res;
    }

    void search(vector<int>& nums, vector<vector<int>>& res, vector<int>& curr, int i) {
        if (i == nums.size()) {
            res.push_back(curr);
            return;
        }

        curr.push_back(nums[i]);
        search(nums, res, curr, i + 1);
        curr.pop_back();

        while (i + 1 < nums.size() && nums[i + 1] == nums[i]) {
            ++i;
        }
        search(nums, res, curr, i + 1);
    }
};
