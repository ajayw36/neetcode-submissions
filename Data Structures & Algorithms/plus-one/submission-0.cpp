class Solution {
public:
    void add(vector<int>& digits, int i) {
        if (digits[i] != 9) {
            digits[i] += 1;
            return;
        }
        else if (i == 0) {
            digits[i] = 0;
            digits.insert(digits.begin(), 1);
            return;
        }
        digits[i] = 0;
        add(digits, i - 1);


    }
    vector<int> plusOne(vector<int>& digits) {
        add(digits, digits.size() - 1);
        return digits;
    }
};
