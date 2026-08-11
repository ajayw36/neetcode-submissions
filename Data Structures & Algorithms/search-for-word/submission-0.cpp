class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        vector<vector<bool>> searched(board.size(), vector<bool>(board[0].size(), false));
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (dfs(board, searched, word, i, j, 0)) return true;
            }
        }

        return false;

    }

    bool dfs(vector<vector<char>>& board, vector<vector<bool>>& searched, string& word, int i, int j, int n) {
        if (board[i][j] != word[n]) return false;
        if (n == word.size() - 1) return true;

        searched[i][j] = true;
        bool b1 = false, b2 = false, b3 = false, b4 = false;
        if (j + 1 < board[0].size() && searched[i][j+1] == false) {
            b1 = dfs(board, searched, word, i, j + 1, n + 1);
        }
        if (i + 1 < board.size() && searched[i + 1][j] == false) {
            b2 = dfs(board, searched, word, i + 1, j, n + 1);
        }
        if (j - 1 >= 0 && searched[i][j-1] == false) {
            b3 = dfs(board, searched, word, i, j - 1, n + 1);
        }
        if (i - 1 >= 0 && searched[i-1][j] == false) {
            b4 = dfs(board, searched, word, i - 1, j, n + 1);
        }
        searched[i][j] = false;

        return b1 || b2 || b3 || b4;
    }
};
