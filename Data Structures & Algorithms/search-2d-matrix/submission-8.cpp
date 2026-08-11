class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0;
        int r = matrix.size() - 1;
        int m = -1;

        while (l <= r) {
            m = (l + r) / 2;

            if (matrix[m][0] == target) {
                return true;
            }
            else if (matrix[m][0] > target) {
                r = m - 1;
            }
            else if (matrix[m][matrix[m].size() - 1] < target){
                l = m + 1;
            }
            else {
                break;
            }
        }

        if (m == -1) {return false;}

        vector<int> nums = matrix[m];
        l = 0;
        r = nums.size() - 1;

        while (l <= r){
            m = (l + r) / 2;
            if (nums[m] == target) {
                return true;
            }
            else if (nums[m] < target) {
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }

        return false;
    }
};
