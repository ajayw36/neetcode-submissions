class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = defaultdict(int)

        i = j = 0
        have, need = 0, len(t)
        res, res_len =  '', float('inf')

        while j < len(s):
            ch_j = s[j]
            if ch_j in count_t and count_s[ch_j] < count_t[ch_j]:
                have += 1
            count_s[ch_j] += 1

            while have == need:
                new_res = s[i:j+1]
                new_len = len(new_res)
                if new_len < res_len:
                    res_len = new_len
                    res = new_res

                ch_i = s[i]
                count_s[ch_i] -= 1
                if ch_i in count_t and count_s[ch_i] < count_t[ch_i]:
                    have -= 1
                i += 1

            j += 1

        return res
