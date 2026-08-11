class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        
        for s in strs:
            char_map = [0] * 26
            for ch in s:
                char_map[ord(ch) - ord('a')] += 1
            if tuple(char_map) in words:
                words[tuple(char_map)].append(s)
            else:
                words[tuple(char_map)] = [s]        
        return list(words.values())
