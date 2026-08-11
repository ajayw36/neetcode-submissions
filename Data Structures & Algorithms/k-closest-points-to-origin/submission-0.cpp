    
class Solution {
public:
    struct compare_points {
        double norm(const vector<int>& point) {
            return sqrt(point[0]*point[0] + point[1]*point[1]);
        }
        bool operator()(const vector<int>& a, const vector<int>& b) {
            return norm(a) > norm(b);
        }
    };

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, compare_points> heap(points.begin(), points.end(), compare_points());
        vector<vector<int>> answer;
        while (k > 0) {
            answer.push_back(heap.top());
            heap.pop();
            --k;
        }
        return answer;
    }

    
};
