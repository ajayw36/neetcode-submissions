class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_size = 0;
        int rows = grid.size();
        int columns = grid[0].size();

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < columns; ++j) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0;
                    int size = 0;
                    stack<pair<int, int>> stack;
                    stack.push({i,j});
                    while(!stack.empty()) {
                        pair<int, int> cell = stack.top();
                        stack.pop();
                        ++size;
                        int r = cell.first;
                        int c = cell.second;

                        if (r + 1 < rows && grid[r + 1][c] == 1) {
                            grid[r + 1][c] = 0;
                            stack.push({r + 1, c});
                        }
                        if (c + 1 < columns && grid[r][c + 1] == 1) {
                            grid[r][c + 1] = 0;
                            stack.push({r, c + 1});
                        }
                        if (r - 1 >= 0 && grid[r - 1][c] == 1) {
                            grid[r - 1][c] = 0;
                            stack.push({r - 1, c});
                        }
                        if (c - 1 >= 0 && grid[r][c - 1] == 1) {
                            grid[r][c - 1] = 0;
                            stack.push({r, c - 1});
                        } 

                    }

                    max_size = max(size, max_size);
                }
            }
        }

        return max_size;
    }
};
