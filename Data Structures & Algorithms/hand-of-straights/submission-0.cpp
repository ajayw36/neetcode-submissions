class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
            std::sort(hand.begin(), hand.end());
            unordered_map<int, int> freq;
            for (int card : hand) {
                    freq[card] += 1;
            }
            int card = hand[0];
            while (true) {
                    for (int i = 0; i < groupSize; ++i) {
                            if (freq[card] == 0) {
                                    return false;
                            }
                            --freq[card];
                            ++card;
                    }
                    card = -1;
                    for (int c : hand) {
                            if (freq[c] != 0) {
                                    card = c;
                                    break;
                            }
                    }
                    if (card == -1) return true;
            }

    }
};