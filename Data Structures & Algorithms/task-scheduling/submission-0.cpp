class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26);
        for (char task : tasks) {
            ++freq[task - 'A'];
        }
        
        priority_queue<int> maxHeap;
        for (int frq: freq) {
           if (frq > 0) maxHeap.push(frq); 
        }

        int count = 0;
        int time = 0;

        while (!maxHeap.empty()) {
            vector<int> removed;
            int cycle = n + 1;
            count = 0;
            while (cycle-- > 0 && !maxHeap.empty()) {
                ++count;
                int k = maxHeap.top();
                if (k > 1) removed.push_back(k - 1);
                maxHeap.pop();
            }
            for (int k : removed) {
                maxHeap.push(k);
            }
            if (maxHeap.empty()) time += count;
            else time += n + 1;
        }

        return time;
    }
};
