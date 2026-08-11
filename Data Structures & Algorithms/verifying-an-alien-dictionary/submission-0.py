class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1: return True

        weights = defaultdict(int)
        for i, ch in enumerate(order):
            weights[ch] = i
            
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            j = 0
            same_word = True
            while j < len(word1) and j < len(word2):
                if weights[word1[j]] < weights[word2[j]]:
                    same_word = False
                    break
                if weights[word1[j]] > weights[word2[j]]: return False
                j += 1
            if same_word and j < len(word1): return False
        
        return True