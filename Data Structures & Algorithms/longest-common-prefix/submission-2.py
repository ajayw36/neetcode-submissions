class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or str[i] != strs[0][i]:
                    return str[:i]
        return strs[0]