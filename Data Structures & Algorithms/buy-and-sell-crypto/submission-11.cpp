class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i = 0;
        int j = 0;
        int res;
        while (j < prices.size()) {
            if (prices[j] < prices[i]) {
                i = j;
            }
            res = max(prices[j] - prices[i], res);
            ++j;
        }
        return res;
    }

    
};
