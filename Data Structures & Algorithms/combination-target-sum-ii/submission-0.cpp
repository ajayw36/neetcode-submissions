class Solution {
public:
    vector<vector<int>> res;
    unordered_map<int, int> count;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> curr;
        vector<int> nums;
        for (int candidate : candidates) {
            if (!count[candidate]) {
                nums.push_back(candidate);
            }
            count[candidate] += 1;
        }
        search(nums, target, curr, 0);
        return res;
    }
    void search(vector<int>& nums, int target, vector<int>& curr, int i) {
        if (target == 0) {
            res.push_back(curr);
            return;
        }
        if (target < 0 || i >= nums.size()) {
            return;
        }

        if (count[nums[i]]) {
            curr.push_back(nums[i]);
            count[nums[i]]--;
            search(nums, target - nums[i], curr, i);
            curr.pop_back();
            count[nums[i]]++;
        }

        search(nums, target, curr, i + 1);
    }
};
