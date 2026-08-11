    
class Solution {
public:
    struct compare_points {
        double norm_square(const vector<int>& point) {
            return point[0]*point[0] + point[1]*point[1];
        }
        bool operator()(const vector<int>& a, const vector<int>& b) {
            return norm_square(a) < norm_square(b);
        }
    };
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, compare_points> heap;
        vector<vector<int>> answer;
        for (int i = 0; i < points.size(); ++i) {
            heap.push(points[i]);
            if (heap.size() > k) {
                heap.pop();
            }
        }
        while (!heap.empty()) {
            vector<int> point = heap.top();
            heap.pop();
            answer.push_back(point);
        }

        return answer;
    }
};
