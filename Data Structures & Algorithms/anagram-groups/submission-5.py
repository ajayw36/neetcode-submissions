class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            charMap = [0] * 26
            for ch in str:
                charMap[ord(ch) - 97] += 1
            
            anagrams.setdefault(tuple(charMap), []).append(str)
        
        res = []
        for anagram in anagrams:
            res.append(anagrams[anagram])
        
        return res