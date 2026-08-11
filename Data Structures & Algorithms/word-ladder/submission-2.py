class Solution:
    def generate_patterns(self, word):
        res = []
        for i in range(len(word)):
            res.append(word[:i] + "*" + word[i+1:])
        return res

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        pattern_map = defaultdict(list)
        for word in wordList:
            for pattern in self.generate_patterns(word):
                pattern_map[pattern].append(word)
        
        q = collections.deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for pattern in self.generate_patterns(word):
                    for nei in pattern_map[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        
        return 0
