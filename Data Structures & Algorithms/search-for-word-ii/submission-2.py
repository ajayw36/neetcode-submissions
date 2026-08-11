class TrieNode:
    def __init__ (self):
        self.children = {}
        self.word = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)
        
        ROWS, COLS = len(board), len(board[0])
        visited, res = set(), set()
        
        def dfs(r, c, node, curr):
            if node.word:
                res.add(curr)
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if (0 <= r + dr < ROWS and 0 <= c + dc < COLS 
                and board[r + dr][c + dc] in node.children 
                and (r + dr, c + dc) not in visited):
                    ch = board[r + dr][c + dc]
                    visited.add((r + dr, c + dc))
                    dfs(r + dr, c + dc, node.children[ch], curr + ch)
                    visited.remove((r + dr, c + dc))

        for r in range(ROWS):
            for c in range(COLS):
                ch = board[r][c]
                if ch in root.children:
                    visited.add((r, c))
                    dfs(r, c, root.children[ch], ch)
                    visited.remove((r, c))
        
        return list(res)
                