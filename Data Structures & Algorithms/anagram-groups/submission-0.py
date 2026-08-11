class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            arr =  [0] * 26
            for ch in word:
                arr[ord(ch) - 97] += 1

            hashmap[tuple(arr)] = [word] + hashmap.get(tuple(arr), [])
        
        return hashmap.values()