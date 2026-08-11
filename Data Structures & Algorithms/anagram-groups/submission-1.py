class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            map = [0]*26
            for ch in str:
                map[ord(ch)-ord('a')] += 1
            res[tuple(map)] = res.get(tuple(map), []) + [str]
        return list(res.values())

