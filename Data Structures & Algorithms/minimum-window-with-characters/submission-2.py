class Solution:
    def compare_counts(self, count_s, count_t):
        for i, count in count_t.items():
            if count_s[i] < count: return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        res = s + ' '
        count_s = defaultdict(int)
        count_t = Counter(t)

        i = 0
        for j in range(len(s)):
            count_s[s[j]] += 1
            while self.compare_counts(count_s, count_t):
                if len(s[i:j+1]) < len(res):
                    res = s[i:j+1]
                count_s[s[i]] -= 1
                i += 1
        
        if len(res) > len(s): return ''
        return res