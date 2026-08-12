class Solution {
public:
    vector<int> partitionLabels(string s) {
            unordered_map<char, int> freq;
            unordered_map<char, int> part;
            vector<int> res;

            for (char c : s) freq[c] += 1;

            for (char c : s) {
                part[c] += 1;
                bool complete = true;
                for (auto& [ch, cnt] : part) {
                        if (freq[ch] != cnt) {
                                complete = false;
                                break;
                        }
                }
                if (complete) {
                        int count = 0;
                        for (auto& [ch, cnt] : part)  {
                                count += cnt;
                        }
                        part.clear();
                        res.push_back(count);
                }
            }

            return res;


    }
};