class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i = 0;
        int j = 0;
        int n = prices.size();
        int res = 0;

        while (j < n) {
            res = std::max(res, prices[j] - prices[i]);
            if (prices[j] < prices[i]) {
                i = j;
            } 
            ++j;
        }

        return res;
    }
};
