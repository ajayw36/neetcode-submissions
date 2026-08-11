class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = {c : set() for w in words for c in w}
        indeg = {c : 0 for c in graph}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indeg[w2[j]] += 1
                    break

        
        q = deque([c for c in indeg if indeg[c] == 0])
        res = []

        while q:
            curr = q.popleft()
            res.append(curr)

            for nei in graph[curr]:
                indeg[nei] -= 1

                if indeg[nei] == 0:
                    q.append(nei)

        
        if len(res) != len(indeg):
            return ""
        
        return "".join(res)
        



            



        
