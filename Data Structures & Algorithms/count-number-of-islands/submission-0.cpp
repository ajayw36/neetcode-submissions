class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        int rows = grid.size();
        int columns = grid[0].size();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (grid[i][j] == '1') {
                    res += 1;
                    stack<pair<int, int>> stack;
                    stack.push({i, j});
                    while (!stack.empty()) {
                        pair<int, int> cell = stack.top();
                        stack.pop();
                        int r = cell.first;
                        int c = cell.second;
                        grid[r][c] = '0';

                        if (r + 1 < rows && grid[r + 1][c] == '1') {
                            stack.push({r + 1, c});
                        }
                        if (r - 1 >= 0 && grid[r - 1][c] == '1') {
                            stack.push({r - 1, c});
                        }
                        if (c + 1 < columns && grid[r][c + 1] == '1') {
                            stack.push({r, c + 1});
                        }
                        if (c - 1 >= 0 && grid[r][c - 1] == '1') {
                            stack.push({r, c - 1});
                        }
                    }
                }
            }
        }

        return res;
        
    }
};
