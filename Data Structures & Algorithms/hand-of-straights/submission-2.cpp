class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
            if (hand.size() % groupSize != 0) return false;
            sort(hand.begin(), hand.end());
            unordered_map<int, int> freq;
            for (int card : hand) freq[card] += 1;

            for (int card : hand) {
                    if (freq[card] == 0) continue;
                    for (int i = 0; i < groupSize; ++i) {
                            if (! (freq[card + i] >= 1)) return false;
                            --freq[card + i];
                    }
            }
            return true;
    }
};