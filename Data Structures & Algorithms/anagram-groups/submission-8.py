from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for str in strs:
            freq = [0] * 26
            for ch in str:
                freq[ord(ch)-ord('a')] += 1
            dict[tuple(freq)].append(str)
        return list(dict.values())