class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26);
        for (char task : tasks) {
            ++freq[task - 'A'];
        }
        
        int maxf = *max_element(freq.begin(), freq.end());
        int maxCount = 0;
        for (int i : freq) {
            if (i == maxf) {
                maxCount++;
            }
        }

        int time = (maxf - 1) * (n + 1) + maxCount;
        return max((int)tasks.size(), time);

    }
};
