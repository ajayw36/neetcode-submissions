class Solution {
public:
    bool isHappy(int n) {
        int slow = n;
        int fast = next_number(n);

        while (slow != fast) {
            fast = next_number(fast);
            fast = next_number(fast);
            slow = next_number(slow);
        }
        return fast == 1;
    }

    int next_number(int n) {
        int output = 0;
        while (n != 0) {
            output += (n % 10) * (n % 10);
            n /= 10;
        }
        return output;
    }
};
