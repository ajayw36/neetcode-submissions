class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = [defaultdict(set) for _ in range(3)]
        for square in range(9):
            row_offset = square // 3
            col_offset = square % 3
            for r in range(3 * row_offset, 3 * row_offset + 3):
                for c in range(3 * col_offset, 3 * col_offset + 3):
                    num = board[r][c]
                    if board[r][c] != '.':
                        if num in rows[r] or num in cols[c] or num in squares[square]:
                            return False
                        rows[r].add(num)
                        cols[c].add(num)
                        squares[square].add(num)
        
        return True