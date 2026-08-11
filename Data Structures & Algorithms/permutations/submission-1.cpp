class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> curr;
        set<int> nums_set(nums.begin(), nums.end());
        search(res, curr, nums_set, nums.size());
        return res;
    }
    void search(vector<vector<int>>& res, vector<int>& curr, set<int>& nums, int n) {
        if (curr.size() == n) {
            res.push_back(curr);
            return;
        }
        for (int i : nums) {
            curr.push_back(i);
            nums.erase(i);
            search(res, curr, nums, n);
            nums.insert(i);
            curr.pop_back();
        }
    }
};
