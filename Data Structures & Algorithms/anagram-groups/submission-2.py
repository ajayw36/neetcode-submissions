class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            map = [0] * 26
            for ch in str:
                map[ord(ch) - ord('a')] += 1
            res[tuple(map)].append(str)
        return list(res.values())
